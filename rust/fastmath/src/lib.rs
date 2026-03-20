use pyo3::prelude::*;

/// Сумма квадратов чисел
#[pyfunction]
fn sum_squares(numbers: Vec<i64>) -> i64 {
    numbers.iter().map(|x| x * x).sum()
}

/// Структура Point
#[pyclass]
struct Point {
    #[pyo3(get, set)]
    x: f64,
    #[pyo3(get, set)]
    y: f64,
}

#[pymethods]
impl Point {
    #[new]
    fn new(x: f64, y: f64) -> Self {
        Point { x, y }
    }

    fn distance(&self, other: &Point) -> f64 {
        let dx = self.x - other.x;
        let dy = self.y - other.y;
        (dx * dx + dy * dy).sqrt()
    }

    fn __repr__(&self) -> String {
        format!("Point(x={}, y={})", self.x, self.y)
    }
}

#[pymodule]
fn fastmath(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_squares, m)?)?;
    m.add_class::<Point>()?;
    Ok(())
}

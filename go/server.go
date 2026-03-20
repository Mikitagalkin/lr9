package main

import (
    "encoding/json"
    "fmt"
    "net/http"
)

type Request struct {
    Numbers []int `json:"numbers"`
}

type Response struct {
    Sum int `json:"sum"`
}

func calculateHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method != http.MethodPost {
        http.Error(w, "Only POST allowed", http.StatusMethodNotAllowed)
        return
    }

    var req Request
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    sum := 0
    for _, n := range req.Numbers {
        sum += n * n
    }

    resp := Response{Sum: sum}
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(resp)
}

func main() {
    http.HandleFunc("/calculate", calculateHandler)
    fmt.Println("Server listening on :8080")
    http.ListenAndServe(":8080", nil)
}
#[macro_use] extern crate cpython;

use cpython::{PyObject, PyResult, Python, PyList};

py_module_initializer!(_tmrs, init_tmrs, PyInit__tmrs, |py, m| {
    try!(m.add(py, "__doc__", "This module is implemented in Rust."));
    try!(m.add(py, "test", py_fn!(py, test_py(data: Vec<f64>))));
    try!(m.add(py, "solve", py_fn!(py, solve_py(
        ma: Vec<f64>, mb: Vec<f64>, mc: Vec<f64>, v: Vec<f64>))));
    try!(m.add(py, "check_convergence", py_fn!(py, check_convergence_py(
        ma: Vec<f64>, mb: Vec<f64>, mc: Vec<f64>, v: Vec<f64>))));
    Ok(())
});

// logic implemented as a normal rust function
fn sum_as_string(a:i64, b:i64) -> String {
    format!("{}", a + b).to_string()
}

fn to_vec<T>(py: Python, list: PyList) -> PyResult<Vec<T>> {
    let length = list.len(py);
    let vec = Vec::with_capacity(length);
    for i in 0..length {

    }
    Ok(vec)
}

fn test_py(py: Python, data: Vec<f64>) -> PyResult<bool> {
    Ok(true)
}

fn solve_py(_: Python, ma: Vec<f64>, mb: Vec<f64>, mc: Vec<f64>, v: Vec<f64>) -> PyResult<Vec<f64>> {
    let size = v.len();
    let mut c: Vec<f64> = Vec::with_capacity(size);
    let mut d: Vec<f64> = Vec::with_capacity(size);
    c.push(-mc[0]/mb[0]);
    d.push(v[0]/mb[0]);
    for i in 1..size {
        let divisor = ma[i] * c[i-1] + mb[i];
        c.push(-mc[i] / divisor);
        let dv = (v[i] - ma[i] * d[i-1]) / divisor;
        d.push(dv);
    }
    let mut result: Vec<f64> = vec![0.0; size];
    result[size-1] = d[size-1];
    let mut i = size-2;
    loop {
        result[i] = c[i] * result[i+1] + d[i];
        if i == 0 { break; }
        i -= 1;
    }
    Ok(result)
}

fn check_convergence_py(_: Python, ma: Vec<f64>, mb: Vec<f64>, mc: Vec<f64>, v: Vec<f64>) -> PyResult<bool> {
    Ok(true)
}

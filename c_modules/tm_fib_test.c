#define PY_SSIZE_T_CLEAN

#include <Python.h>

int fib(int n)
{
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-1);
}

PyObject* c_fib(PyObject* self, PyObject* args)
{
    int n;
    PyArg_ParseTuple(args, "i", &n);
    n = fib(n);
    return PyLong_FromLong(n);
}

PyMethodDef module_methods[] =
{
    {"c_fib", c_fib, METH_VARARGS, "Recursive Fibonacci function"},
    {NULL, NULL, 0, NULL}
};

struct PyModuleDef c_module =
{
    PyModuleDef_HEAD_INIT,
    "c_module",
    "Test module",
    -1,
    module_methods
};

PyMODINIT_FUNC PyInit_c_module()
{
    return PyModule_Create(&c_module);
}

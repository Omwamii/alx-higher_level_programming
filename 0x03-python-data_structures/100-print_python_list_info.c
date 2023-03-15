#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints info about python list
 * @p: list object struct
 *
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *py = (PyListObject *)p;
	Py_ssize_t i = 0, size = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", py->allocated);

	for (; i < size; i++)
		printf("Element %li: %s\n", i, Py_TYPE(py->ob_item[i])->tp_name);
}

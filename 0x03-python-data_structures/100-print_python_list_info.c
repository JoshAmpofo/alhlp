#include <Python.h>
/**
 * print_python_list_info - Prints basic info about Python Lists
 * @p: A PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size, i, alloc;
	PyObject *obj;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		PyObject = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(PyObject)->tp_name);
	}
}

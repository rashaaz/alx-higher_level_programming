#include <Python.h>

/**
 * print_python_list_info - Prints basic information
 * @p: Pointer
 */
void print_python_list_info(PyObject *p)
{
	int size, al, i;
	PyObject *bi;

	size = Py_SIZE(p);
	al = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", al);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		bi = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(bi)->tp_name);
	}
}

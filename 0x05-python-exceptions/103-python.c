#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <floatobject.h>

/**
 * print_python_list - Prints basic information
 * @p: Pointer
 */
void print_python_list(PyObject *p)
{
	int i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
				((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints information about a Python
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
	size_t i, le, size;
	char *st;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	st =  ((PyBytesObject *)p)->ob_sval;
	le = size + 1 > 10 ? 10 : size + 1;
	printf("  size: %lu\n", size);
	printf("  trying string: %s\n", st);
	printf("  first %lu bytes: ", le);
	for (i = 0; i < le; i++)
		printf("%02hhx%s", st[i], i + 1 < le ? " " : "");

	printf("\n");
}

/**
 * print_python_float - Prints information Python float
 * @p: PyObject pointer
 */
void print_python_float(PyObject *p)
{
	double e;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	e = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s/n",
			PyOS_double_to_string(e, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

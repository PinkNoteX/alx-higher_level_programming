#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - print list info
 * @p: pyobject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *i;
	PyListObject *list;
	long int s, x;

	s = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", s);
	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	x = 0;
	while (x < s)
	{
		i = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", x, Py_TYPE(i)->tp_name);
		x++;
	}

}

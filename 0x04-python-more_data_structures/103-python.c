#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 * @p: python obj
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int i, lim, s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", s);
	printf("  trying string: %s\n", str);

	if (s >= 10)
		lim = 10;
	else
		lim = s + 1;
	printf("  first %ld bytes:", lim);
	for (i = 0; i < lim; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	printf("\n");
}
/**
 * print_python_list - Prints python list info
 * @p: python object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *ob;
	PyListObject *list;
	long int s, x;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	x = 0;
	while (x < s)
	{
		ob = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((ob)->ob_type)->tp_name);
		if (PyBytes_Check(ob))
			print_python_bytes(ob);
	x++;
	}
}

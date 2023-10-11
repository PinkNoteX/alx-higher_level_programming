#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/*
 * print_python_list - Prints python list info
 * @p: python object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	PyObject *i;
	PyListObject *list;
	long int s, x;

	s = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < s; x++)
	{
		i = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((i)->ob_type)->tp_name);
		if (PyBytes_Check(i))
			print_python_bytes(i);
	}
}
/*
 * print_python_bytes - Prints bytes information
 * @p: python obj
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	char *str;
	long int s, x, r;
	
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
	{
		r = 10;
	}
	else
	{
		r = s + 1;
	}

	printf("  first %ld bytes:", r);
	x = 0;
	while (x < r)
	{
		if (str[x] >= 0)
			printf(" %02x", str[x]);
		else
			printf(" %02x", 256 + str[x]);
	printf("\n");
	x++;
	}
}

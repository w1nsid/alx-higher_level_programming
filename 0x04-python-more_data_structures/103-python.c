#include <stdio.h>
#include <Python.h>

/**
 * display_python_bytes - Displays byte object information
 *
 * @py_object: Python Object
 * Return: None
 */
void print_python_bytes(PyObject *py_object)
{
	char *byte_str;
	long int byte_size, index, byte_limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py_object))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)(py_object))->ob_size;
	byte_str = ((PyBytesObject *)py_object)->ob_sval;

	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", byte_str);

	byte_limit = byte_size >= 10 ? 10 : byte_size + 1;

	printf("  first %ld bytes:", byte_limit);

	for (index = 0; index < byte_limit; index++)
		if (byte_str[index] >= 0)
			printf(" %02x", byte_str[index]);
		else
			printf(" %02x", 256 + byte_str[index]);

	printf("\n");
}

/**
 * display_python_list - Displays list information
 *
 * @py_object: Python Object
 * Return: None
 */
void print_python_list(PyObject *py_object)
{
	long int list_size, index;
	PyListObject *py_list;
	PyObject *list_element;

	list_size = ((PyVarObject *)(py_object))->ob_size;
	py_list = (PyListObject *)py_object;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", py_list->allocated);

	for (index = 0; index < list_size; index++)
	{
		list_element = ((PyListObject *)py_object)->ob_item[index];
		printf("Element %ld: %s\n", index, ((list_element)->ob_type)->tp_name);
		if (PyBytes_Check(list_element))
			print_python_bytes(list_element);
	}
}

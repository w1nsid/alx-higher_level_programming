#include "Python.h"

/**
 * display_python_string_info - Prints details about Python string objects.
 * @py_obj: A PyObject string object.
 */
void display_python_string_info(PyObject *py_obj)
{
	long int str_length;

	fflush(stdout);

	printf("[.] String object info:\n");
	if (strcmp(py_obj->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	str_length = ((PyASCIIObject *)(py_obj))->length;

	if (PyUnicode_IS_COMPACT_ASCII(py_obj))
		printf("  Type: compact ascii\n");
	else
		printf("  Type: compact unicode object\n");
	printf("  Length: %ld\n", str_length);
	printf("  Value: %ls\n", PyUnicode_AsWideCharString(py_obj, &str_length));
}

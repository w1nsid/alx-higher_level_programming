#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints basic info about Python lists
 * @p: pointer to the Python list object
 * description: prints some basic info about Python lists
 */
void print_python_list_info(PyObject *p)
{
	long int listSize = PyList_Size(p);
	int iterator;

	PyListObject *pythonList = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", listSize);
	printf("[*] Allocated = %li\n", pythonList->allocated);

	for (iterator = 0; iterator < listSize; iterator++)
		printf("Element %i: %s\n", iterator, Py_TYPE(pythonList->ob_item[iterator])->tp_name);
}

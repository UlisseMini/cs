#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

void* my_malloc(size_t size, const char* file, int line) {
  void* ptr = malloc(size);
  printf("[%s:%d] malloc(%lu) = %p\n", file, line, size, ptr);
  return ptr;
}

void my_free(void *ptr, const char* file, int line) {
  free(ptr);
  printf("[%s:%d] free(%p)\n", file, line, ptr);
}

void* my_calloc(size_t nmemb, size_t size, const char* file, int line) {
  void* ptr = calloc(nmemb, size);
  printf("[%s:%d] calloc(%lu, %lu) = %p\n", file, line, nmemb, size, ptr);
  return ptr;
}

void* my_realloc(void *ptr, size_t size);

/* void* my_reallocarray(void *ptr, size_t nmemb, size_t size); */

#define calloc(nmemb, size) my_calloc(nmemb, size, __FILE__, __LINE__)
#define malloc(size) my_malloc(size, __FILE__, __LINE__)
#define free(ptr) my_free(ptr, __FILE__, __LINE__)



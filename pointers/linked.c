#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
// #include "memdebug.h"

// This is written in a terrible heap-allocate everything style to practice my C.

typedef struct list {
  struct list* next;
  struct list* prev;
  char* value;
} list;


list* list_malloc(char* value) {
  list* l = malloc(sizeof(list));
  assert(l != NULL);
  l->next = NULL, l->prev = NULL;
  l->value = malloc(sizeof(char) * strlen(value));
  assert(l->value != NULL);
  strcpy(l->value, value);

  return l;
}

list* list_tail(list* l) {
  list* curr = l;
  for (; curr->next != NULL; curr = curr->next) {}
  return curr;
}

void list_add(list* l, char* value) {
  list* tail = list_tail(l);
  assert(tail->next == NULL);
  tail->next = list_malloc(value);
  tail->next->prev = tail;
}

list* list_find_after(list* l, char* value) {
  for (list* curr = l; curr != NULL; curr = curr->next) {
    if (strcmp(curr->value, value) == 0) {
      return curr;
    }
  }
  return NULL;
}

// Free a node, if the node is connected to a list this will leave dangling pointers.
void list_free(list* node) {
  free(node->value);
  free(node);
}

// Free all nodes after l, including itself, for the head node this frees the entire list.
void list_free_after(list* l) {
  list* curr = l;
  list* next;
  while (curr != NULL) {
    next = curr->next;
    list_free(curr);
    curr = next;
  }
}

// free a node and adjust adjacent node pointers
void list_delete_node(list* node) {
  if (node->next) { node->next->prev = node->prev; }
  if (node->prev) { node->prev->next = node->next; }
  list_free(node);
}

// find and delete a node by value
void list_delete(list* l, char* value) {
  list* node = list_find_after(l, value);
  list_delete_node(node);
}

char* list_stringify(list* l) {
  // purposely tiny cap to practice realloc
  int capacity = 2;
  char* buf = malloc(capacity); // sizeof(char) = 1 (1 byte)
  memset(buf, 0, capacity); // memset or strlen breaks

  for (list* curr = l; curr != NULL; curr = curr->next) {
    // add space for newline and nullbyte
    size_t required = strlen(buf) + strlen(curr->value) + 2;
    if (required > capacity) {
      /* printf("required %d had %d for '%s' + '%s\\n'\n", required, capacity, buf, curr->value); */
      buf = realloc(buf, required);
      assert(buf != NULL);
      capacity = required;
    }

    sprintf(buf + strlen(buf), "%s\n", curr->value);
  }

  return buf;
}

int main() {
  printf("start\n");
  list* l = list_malloc("foo");
  list_add(l, "bar");
  list_add(l, "baz");
  list_add(l, "qux");

  list* node = list_find_after(l, "baz");
  assert(strcmp(node->value, "baz") == 0);

  list_delete(l, "baz");

  node = list_find_after(l, "baz");
  assert(node == NULL);

  char* str = list_stringify(l);
  printf("list:\n'%s'\n", str);
  free(str);

  list_free_after(l);
  printf("exit 0\n");
  return 0;
}

#ifdef __cplusplus
extern "C" {
#endif

#include <chucknorris_export.h>

/* Preface every function with `chuck_norris` to create a pseude namespace */
/* Use an opaque pointer to refer to ChuckNorris objects in C. 
   typecasts have to be performed in C++. */ 
typedef struct chuck_norris chuck_norris_t;

/* explicit initialization and destruction in C: */
CHUCKNORRIS_EXPORT chuck_norris_t*  chuck_norris_init(void);
CHUCKNORRIS_EXPORT void chuck_norris_deinit(chuck_norris_t*);

/* C API cannot use methods but functions that refer to
   a struct that belongs to an object. */
CHUCKNORRIS_EXPORT char* chuck_norris_get_fact(chuck_norris_t*);

#ifdef __cplusplus
}
#endif
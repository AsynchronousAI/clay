#if !__mcffpu__

#define FLT_EVAL_METHOD 2

#define LDBL_TRUE_MIN 3.6451995318824746025e-4951L
#define LDBL_MIN     1.68105157155604675313e-4932L
#define LDBL_MAX     1.1897314953572317650e+4932L
#define LDBL_EPSILON 1.0842021724855044340e-19L

#define LDBL_MANT_DIG 64
#define LDBL_MIN_EXP (-16382)
#define LDBL_MAX_EXP 16384

#define LDBL_DIG 18
#define LDBL_MIN_10_EXP (-4931)
#define LDBL_MAX_10_EXP 4932

#define DECIMAL_DIG 21

#else

#define FLT_EVAL_METHOD 0

#define LDBL_TRUE_MIN 4.94065645841246544177e-324L
#define LDBL_MIN 2.22507385850720138309e-308L
#define LDBL_MAX 1.79769313486231570815e+308L
#define LDBL_EPSILON 2.22044604925031308085e-16L

#define LDBL_MANT_DIG 53
#define LDBL_MIN_EXP (-1021)
#define LDBL_MAX_EXP 1024

#define LDBL_DIG 15
#define LDBL_MIN_10_EXP (-307)
#define LDBL_MAX_10_EXP 308

#define DECIMAL_DIG 17

#endif
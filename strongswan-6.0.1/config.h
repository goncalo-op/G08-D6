/* config.h.  Generated from config.h.in by configure.  */
/* config.h.in.  Generated from configure.ac by autoheader.  */

/* Define if building universal (internal helper macro) */
/* #undef AC_APPLE_UNIVERSAL_BUILD */

/* capability dropping support */
/* #undef CAPABILITIES */

/* have libpcap library */
/* #undef CAPABILITIES_LIBCAP */

/* have native linux capset() */
/* #undef CAPABILITIES_NATIVE */

/* UDP post used by charon locally in case a NAT is detected */
/* #undef CHARON_NATT_PORT */

/* UDP port used by charon locally */
/* #undef CHARON_UDP_PORT */

/* defined if config.h included */
#define CONFIG_H_INCLUDED /**/

/* Define to 1 if using 'alloca.c'. */
/* #undef C_ALLOCA */

/* Define to 1 if you have 'alloca', as a function or macro. */
#define HAVE_ALLOCA 1

/* Define to 1 if <alloca.h> works. */
#define HAVE_ALLOCA_H 1

/* Define to 1 if you have the `backtrace' function. */
#define HAVE_BACKTRACE 1

/* have binutils bfd.h */
/* #undef HAVE_BFD_H */

/* Define to 1 if you have the `botan_pubkey_ecc_key_used_explicit_encoding'
   function. */
/* #undef HAVE_BOTAN_PUBKEY_ECC_KEY_USED_EXPLICIT_ENCODING */

/* Define to 1 if you have the `botan_rng_init_custom' function. */
/* #undef HAVE_BOTAN_RNG_INIT_CUSTOM */

/* Define to 1 if you have the `chown' function. */
#define HAVE_CHOWN 1

/* Define to 1 if you have the `clock_gettime' function. */
#define HAVE_CLOCK_GETTIME 1

/* Define to 1 if you have the `closefrom' function. */
#define HAVE_CLOSEFROM 1

/* pthread_condattr_setclock supports CLOCK_MONOTONIC */
#define HAVE_CONDATTR_CLOCK_MONOTONIC /**/

/* Define to 1 if you have the declaration of `bfd_get_section_flags', and to
   0 if you don't. */
/* #undef HAVE_DECL_BFD_GET_SECTION_FLAGS */

/* Define to 1 if you have the declaration of `bfd_get_section_size', and to 0
   if you don't. */
/* #undef HAVE_DECL_BFD_GET_SECTION_SIZE */

/* Define to 1 if you have the declaration of `bfd_get_section_vma', and to 0
   if you don't. */
/* #undef HAVE_DECL_BFD_GET_SECTION_VMA */

/* Define to 1 if you have the declaration of `bfd_section_flags', and to 0 if
   you don't. */
/* #undef HAVE_DECL_BFD_SECTION_FLAGS */

/* Define to 1 if you have the declaration of `bfd_section_size', and to 0 if
   you don't. */
/* #undef HAVE_DECL_BFD_SECTION_SIZE */

/* Define to 1 if you have the declaration of `bfd_section_vma', and to 0 if
   you don't. */
/* #undef HAVE_DECL_BFD_SECTION_VMA */

/* Define to 1 if you have the declaration of `strerror_r', and to 0 if you
   don't. */
#define HAVE_DECL_STRERROR_R 1

/* Define to 1 if you have the `dirfd' function. */
#define HAVE_DIRFD 1

/* have dladdr() */
#define HAVE_DLADDR /**/

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Define to 1 if you have the `explicit_bzero' function. */
#define HAVE_EXPLICIT_BZERO 1

/* Define to 1 if you have the `fmemopen' function. */
#define HAVE_FMEMOPEN 1

/* Define to 1 if you have the `funopen' function. */
/* #undef HAVE_FUNOPEN */

/* have GCC __sync_* operations */
#define HAVE_GCC_SYNC_OPERATIONS /**/

/* have GCRY_CIPHER_CAMELLIA128 */
/* #undef HAVE_GCRY_CIPHER_CAMELLIA */

/* Define to 1 if you have the `getgrnam_r' function. */
#define HAVE_GETGRNAM_R 1

/* Define to 1 if you have the `getpass' function. */
#define HAVE_GETPASS 1

/* Define to 1 if you have the `getpwnam_r' function. */
#define HAVE_GETPWNAM_R 1

/* Define to 1 if you have the `getpwuid_r' function. */
#define HAVE_GETPWUID_R 1

/* have gettid() */
#define HAVE_GETTID /**/

/* Define to 1 if you have the <glob.h> header file. */
#define HAVE_GLOB_H 1

/* have struct in6_addr in6addr_any */
#define HAVE_IN6ADDR_ANY /**/

/* have struct in6_pktinfo.ipi6_ifindex */
#define HAVE_IN6_PKTINFO /**/

/* have __int128 type support */
#define HAVE_INT128 /**/

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* have IPSEC_DIR_FWD defined */
#define HAVE_IPSEC_DIR_FWD /**/

/* have IPSEC_MODE_BEET defined */
#define HAVE_IPSEC_MODE_BEET /**/

/* Define to 1 if you have the `gmp' library (-lgmp). */
#define HAVE_LIBGMP 1

/* have libunwind.h */
/* #undef HAVE_LIBUNWIND_H */

/* Define to 1 if you have the <linux/fib_rules.h> header file. */
#define HAVE_LINUX_FIB_RULES_H 1

/* Define to 1 if you have the <linux/udp.h> header file. */
#define HAVE_LINUX_UDP_H 1

/* Define to 1 if you have the <linux/vm_sockets.h> header file. */
#define HAVE_LINUX_VM_SOCKETS_H 1

/* Define to 1 if you have the `mallinfo' function. */
#define HAVE_MALLINFO 1

/* Define to 1 if you have the `mallinfo2' function. */
#define HAVE_MALLINFO2 1

/* Define to 1 if you have the `memrchr' function. */
#define HAVE_MEMRCHR 1

/* Define to 1 if you have the `mmap' function. */
#define HAVE_MMAP 1

/* have mpz_powm_sec() */
#define HAVE_MPZ_POWM_SEC /**/

/* Define to 1 if you have the <netinet6/ipsec.h> header file. */
/* #undef HAVE_NETINET6_IPSEC_H */

/* Define to 1 if you have the <netinet/ip6.h> header file. */
#define HAVE_NETINET_IP6_H 1

/* Define to 1 if you have the <netipsec/ipsec.h> header file. */
/* #undef HAVE_NETIPSEC_IPSEC_H */

/* Define to 1 if you have the <net/if_tun.h> header file. */
/* #undef HAVE_NET_IF_TUN_H */

/* Define to 1 if you have the <net/pfkeyv2.h> header file. */
/* #undef HAVE_NET_PFKEYV2_H */

/* Define to 1 if you have the `prctl' function. */
#define HAVE_PRCTL 1

/* have register_printf_function() */
/* #undef HAVE_PRINTF_FUNCTION */

/* have register_printf_specifier() */
#define HAVE_PRINTF_SPECIFIER /**/

/* Define to 1 if you have the `pthread_cancel' function. */
#define HAVE_PTHREAD_CANCEL 1

/* Define to 1 if you have the `pthread_condattr_init' function. */
#define HAVE_PTHREAD_CONDATTR_INIT 1

/* Define to 1 if you have the `pthread_condattr_setclock' function. */
/* #undef HAVE_PTHREAD_CONDATTR_SETCLOCK */

/* Define to 1 if you have the `pthread_cond_timedwait_monotonic' function. */
/* #undef HAVE_PTHREAD_COND_TIMEDWAIT_MONOTONIC */

/* Define to 1 if you have the `pthread_rwlock_init' function. */
#define HAVE_PTHREAD_RWLOCK_INIT 1

/* Define to 1 if you have the `pthread_spin_init' function. */
#define HAVE_PTHREAD_SPIN_INIT 1

/* have qsort_r() */
#define HAVE_QSORT_R /**/

/* have BSD-style qsort_r() */
/* #undef HAVE_QSORT_R_BSD */

/* have GNU-style qsort_r() */
#define HAVE_QSORT_R_GNU /**/

/* have netlink RTA_TABLE defined */
#define HAVE_RTA_TABLE /**/

/* have PF_ROUTE RTM_IFANNOUNCE defined */
/* #undef HAVE_RTM_IFANNOUNCE */

/* Define to 1 if you have the `sd_listen_fds_with_names' function. */
/* #undef HAVE_SD_LISTEN_FDS_WITH_NAMES */

/* Define to 1 if you have the `sem_timedwait' function. */
#define HAVE_SEM_TIMEDWAIT 1

/* Define to 1 if you have the `setlinebuf' function. */
#define HAVE_SETLINEBUF 1

/* Define to 1 if you have the `sigwaitinfo' function. */
#define HAVE_SIGWAITINFO 1

/* have sqlite3_prepare_v2() */
/* #undef HAVE_SQLITE3_PREPARE_V2 */

/* Define to 1 if stdbool.h conforms to C99. */
#define HAVE_STDBOOL_H 1

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdio.h> header file. */
#define HAVE_STDIO_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define if you have `strerror_r'. */
#define HAVE_STRERROR_R 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the `strptime' function. */
#define HAVE_STRPTIME 1

/* Define to 1 if `sadb_x_policy_priority' is a member of `struct
   sadb_x_policy'. */
#define HAVE_STRUCT_SADB_X_POLICY_SADB_X_POLICY_PRIORITY 1

/* Define to 1 if `sa_len' is a member of `struct sockaddr'. */
/* #undef HAVE_STRUCT_SOCKADDR_SA_LEN */

/* have syslog(3) and friends */
#define HAVE_SYSLOG /**/

/* have sys/capability.h */
/* #undef HAVE_SYS_CAPABILITY_H */

/* have syscall(SYS_gettid) */
/* #undef HAVE_SYS_GETTID */

/* Define to 1 if you have the <sys/param.h> header file. */
#define HAVE_SYS_PARAM_H 1

/* Define to 1 if you have the <sys/sockio.h> header file. */
/* #undef HAVE_SYS_SOCKIO_H */

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/syscall.h> header file. */
#define HAVE_SYS_SYSCALL_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Define to 1 if the system has the type `_Bool'. */
#define HAVE__BOOL 1

/* groupname to run daemon with */
/* #undef IPSEC_GROUP */

/* username to run daemon with */
/* #undef IPSEC_USER */

/* Define to the sub-directory where libtool stores uninstalled libraries. */
#define LT_OBJDIR ".libs/"

/* mediation extension support */
/* #undef ME */

/* monolithic build embedding plugins */
/* #undef MONOLITHIC */

/* Name of package */
#define PACKAGE "strongswan"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT ""

/* Define to the full name of this package. */
#define PACKAGE_NAME "strongSwan"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "strongSwan 6.0.1"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "strongswan"

/* Define to the home page for this package. */
#define PACKAGE_URL ""

/* Define to the version of this package. */
#define PACKAGE_VERSION "6.0.1"

/* If using the C implementation of alloca, define if you know the
   direction of stack growth for your system; otherwise it will be
   automatically deduced at runtime.
	STACK_DIRECTION > 0 => grows toward higher addresses
	STACK_DIRECTION < 0 => grows toward lower addresses
	STACK_DIRECTION = 0 => direction of growth unknown */
/* #undef STACK_DIRECTION */

/* static plugin constructors */
/* #undef STATIC_PLUGIN_CONSTRUCTORS */

/* Define to 1 if all of the C90 standard headers exist (not just the ones
   required in a freestanding environment). This macro is provided for
   backward compatibility; new code need not use it. */
#define STDC_HEADERS 1

/* Define to 1 if strerror_r returns char *. */
/* #undef STRERROR_R_CHAR_P */

/* use TSS2 v2 Extended System API */
/* #undef TSS2_ESYS */

/* use TSS2 v2 System API */
/* #undef TSS2_SYS */

/* use TCTI Sockets */
/* #undef TSS2_TCTI_SOCKET */

/* use TCTI Access Broker and Resource Manager */
/* #undef TSS2_TCTI_TABRMD */

/* use TrouSerS library libtspi */
/* #undef TSS_TROUSERS */

/* use TSS 2.0 v1 libraries */
/* #undef TSS_TSS2_V1 */

/* use TSS 2.0 v2 libraries */
/* #undef TSS_TSS2_V2 */

/* using builtin printf for printf hooks */
/* #undef USE_BUILTIN_PRINTF */

/* build code for fuzzing */
/* #undef USE_FUZZING */

/* support for IKEv1 protocol */
#define USE_IKEV1 /**/

/* support for IKEv2 protocol */
#define USE_IKEV2 /**/

/* build code for JSON */
/* #undef USE_JSON */

/* build with support for SELinux */
/* #undef USE_SELINUX */

/* use thread ID for thread identification, if available */
/* #undef USE_THREAD_IDS */

/* use Vstr string library for printf hooks */
/* #undef USE_VSTR */

/* Version number of package */
#define VERSION "6.0.1"

/* Define WORDS_BIGENDIAN to 1 if your processor stores words with the most
   significant byte first (like Motorola and SPARC, unlike Intel). */
#if defined AC_APPLE_UNIVERSAL_BUILD
# if defined __BIG_ENDIAN__
#  define WORDS_BIGENDIAN 1
# endif
#else
# ifndef WORDS_BIGENDIAN
/* #  undef WORDS_BIGENDIAN */
# endif
#endif

/* Define to 1 if `lex' declares `yytext' as a `char *' by default, not a
   `char[]'. */
#define YYTEXT_POINTER 1

/* Define to `unsigned int' if <sys/types.h> does not define. */
/* #undef size_t */

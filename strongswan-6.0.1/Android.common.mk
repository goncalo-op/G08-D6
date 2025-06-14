# some common definitions used by the main and the NDK-specific Android.mk
# include this after strongswan_PLUGINS has been defined

# helper macros to only add source files for plugins included in the list above
# source files are relative to the android.mk that called the macro
plugin_enabled = $(filter $(1), $(strongswan_PLUGINS))
add_plugin = $(if $(call plugin_enabled,$(1)), \
               $(patsubst $(LOCAL_PATH)/%,%, \
                 $(wildcard \
                   $(subst %,$(subst -,_,$(strip $(1))), \
                     $(LOCAL_PATH)/plugins/%/%*.c \
                    ) \
                  ) \
                ) \
              )
add_plugin_subdirs = $(if $(call plugin_enabled,$(1)), \
               $(patsubst $(LOCAL_PATH)/%,%, \
                 $(wildcard \
                   $(subst %,$(subst -,_,$(strip $(1))), \
                     $(addprefix $(LOCAL_PATH)/plugins/%/,$(addsuffix /*.c, \
                       $(strip $(2)) \
                      )) \
                    ) \
                  ) \
                ) \
              )

# strongSwan version, replaced by top Makefile
strongswan_VERSION := "6.0.1"


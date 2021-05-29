/// ==========================================================
/// Compiler-Generated Header file for Base Content Management
/// ==========================================================
#pragma once

/// Imports
#include <stdbool.h>

#ifndef __PARAC___H_
#define __PARAC___H_

/* If the code is included in an CPP environment which Para-C supports, it will be treated as regular C-code */
#if __cplusplus
extern "C" {
#endif

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// User Project Configuration
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
const char* ph_name_ = "exceptions_example";
const char* ph_description_ = "Example for showing how the exceptions 'should' work";
const char* ph_author_ = "Luna Klatzer";
const char* ph_version_ = "0.1";
const char* ph_license_ = "GPL-3.0";

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Compiler Configuration
/// C-Compiler Paths are included, so that using 'parac finish' the compilation can be automatically finished
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_pcompiler_path_ = "";
const char* ph_ccompiler_path_ = "";

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Types definition - Compiler-Generated
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

/// Exit Status structure storing the basic values for a closing return aka. entry-point function return
typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    int status_code;
} ph_ExitStatus;

/// Type defining the EntryPoint of a Program
typedef union {
    ph_ExitStatus exit_r;
} ph_EntryPoint;

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Function Return Types
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

/// Undefined Base Return which serves as the base for all Return-Types
typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    bool is_null;
} ph_UndefBaseReturn;

/// Para-C Return of Type int. Compiler-Generated
typedef struct {
    ph_UndefBaseReturn base;
    int actual_value;
} ph_ReturnTypeInt;

/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Additional Function declarations
/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

/// Converts the the exit-status to an entry-return type
ph_EntryPoint ExitStatusToEntryReturn(ph_ExitStatus s) { return (ph_EntryPoint) { .exit_r = s }; }

#if __cplusplus
}
#endif

#endif
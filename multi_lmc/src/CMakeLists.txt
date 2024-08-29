cmake_minimum_required(VERSION 3.16.3)

project(MultiDevice VERSION "1.0.0" LANGUAGES C CXX)

# Set the C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(PARENT_DIR "${CMAKE_SOURCE_DIR}/..")
set(ULTRALEAP_PATH_ROOT "${PARENT_DIR}/ext_lib/Ultraleap")

find_package(LeapSDK 5 REQUIRED PATHS "${ULTRALEAP_PATH_ROOT}")

add_executable(MultiDeviceSampleCPP "MultiDeviceSampleCPP.cpp")
set_property(TARGET "MultiDeviceSampleCPP" PROPERTY FOLDER "src")
target_link_libraries(MultiDeviceSampleCPP PUBLIC LeapSDK::LeapC)

get_target_property(
	LEAPC_IMPORTED_CONFIG
	LeapSDK::LeapC
	IMPORTED_CONFIGURATIONS
)

get_target_property(
	LEAPC_SHARED_LIB_PATH
	LeapSDK::LeapC
	IMPORTED_LOCATION_${LEAPC_IMPORTED_CONFIG}
)

add_custom_command(
	TARGET
		MultiDeviceSampleCPP
	POST_BUILD
	COMMAND
		${CMAKE_COMMAND} -E copy
		${LEAPC_SHARED_LIB_PATH}
		$<TARGET_FILE_DIR:MultiDeviceSampleCPP>)

set(FREEGLUT_INCLUDE_DIR "${PARENT_DIR}/ext_lib/freeglut/include") 
set(FREEGLUT_LIB_DIR "${PARENT_DIR}/ext_lib/freeglut/lib/x64")
set(ADDITIONAL_INCLUDE
	${FREEGLUT_INCLUDE_DIR}
	)
set(ADDITIONAL_LIB	
	${FREEGLUT_LIB_DIR}/freeglut.lib 
	${FREEGLUT_LIB_DIR}/glew32.lib
	)

# Add targets for each source file.
function(add_source source_name source_file)

  add_executable(${source_name} ${source_file} ${CMAKE_SOURCE_DIR}/Linking/multiLMC_process.cpp)
  set_property(TARGET ${source_name} PROPERTY FOLDER "src")
  target_link_libraries(${source_name} PUBLIC LeapSDK::LeapC ${ADDITIONAL_LIB})
  target_include_directories(${source_name} PUBLIC ${ADDITIONAL_INCLUDE}) 

endfunction()

add_source("MultiLMC_Plot" "MultiLMC_Plot.cpp")

set(header "${PARENT_DIR}/ext_lib/Alglib/header")
set(src "${PARENT_DIR}/ext_lib/Alglib/src")

include_directories(${header})

set(alglib_header
    ${header}/alglibinternal.h
    ${header}/alglibmisc.h
    ${header}/ap.h
    ${header}/dataanalysis.h
    ${header}/diffequations.h
    ${header}/fasttransforms.h
    ${header}/integration.h
    ${header}/interpolation.h
    ${header}/kernels_avx2.h
    ${header}/kernels_fma.h
    ${header}/kernels_sse2.h
    ${header}/linalg.h
    ${header}/optimization.h
    ${header}/solvers.h
    ${header}/specialfunctions.h
    ${header}/statistics.h
    ${header}/stdafx.h
    )

set(alglib_src
    ${src}/alglibinternal.cpp
    ${src}/alglibmisc.cpp
    ${src}/ap.cpp
    ${src}/dataanalysis.cpp
    ${src}/diffequations.cpp
    ${src}/fasttransforms.cpp
    ${src}/integration.cpp
    ${src}/interpolation.cpp
    ${src}/kernels_avx2.cpp
    ${src}/kernels_fma.cpp
    ${src}/kernels_sse2.cpp
    ${src}/linalg.cpp
    ${src}/optimization.cpp
    ${src}/solvers.cpp
    ${src}/specialfunctions.cpp
    ${src}/statistics.cpp
    )

set(interp_header
    ${header}/alglibinternal.h
    ${header}/alglibmisc.h
    ${header}/ap.h
    ${header}/integration.h
    ${header}/interpolation.h
    ${header}/linalg.h
    ${header}/optimization.h
    ${header}/solvers.h
    ${header}/specialfunctions.h
    ${header}/stdafx.h
    )

set(interp_src
    ${src}/alglibinternal.cpp
    ${src}/alglibmisc.cpp
    ${src}/ap.cpp
    ${src}/integration.cpp
    ${src}/interpolation.cpp
    ${src}/linalg.cpp
    ${src}/optimization.cpp
    ${src}/solvers.cpp
    ${src}/specialfunctions.cpp
    )

function(add_source_alglib source_name source_file)
    add_executable(${source_name} ${source_file} ${interp_src} ${CMAKE_SOURCE_DIR}/Linking/multiLMC_process.cpp)
    target_include_directories(${source_name} PUBLIC ${interp_header})   
endfunction()

add_source_alglib("MultiLMC_Interpolate" "MultiLMC_Interpolate.cpp")

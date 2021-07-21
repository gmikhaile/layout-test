include(GenerateExportHeader)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(HELLO_PUBLIC_HEADERS
	PrintHello.h
)

file(GLOB HELLO_SOURCES LIST_DIRECTORIES=false *.cpp)

add_library(${PROJECT_NAME}
	${HELLO_PUBLIC_HEADERS}
    ${HELLO_SOURCES}
)

set_target_properties(${PROJECT_NAME} PROPERTIES
	DEFINE_SYMBOL HELLO
)

generate_export_header(${PROJECT_NAME}
	 EXPORT_FILE_NAME "${CMAKE_CURRENT_BINARY_DIR}/include/exports.h"
)

message(${CMAKE_CURRENT_SOURCE_DIR})

target_include_directories(${PROJECT_NAME}
	PUBLIC
		$<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/include>
	INTERFACE
		$<INSTALL_INTERFACE:include>
)

install(FILES 
	${HELLO_PUBLIC_HEADERS}
	"${CMAKE_CURRENT_BINARY_DIR}/include/exports.h"
	DESTINATION "include")

install(TARGETS ${PROJECT_NAME}
	EXPORT ${HELLO_EXPORT_NAME}
)
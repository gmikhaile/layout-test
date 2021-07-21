cmake_minimum_required(VERSION 3.15.7)

project(hello VERSION 0.1.0 LANGUAGES CXX)

# project variables
set(HELLO_PACKAGE_NAME ${PROJECT_NAME})
set(HELLO_EXPORT_NAME ${HELLO_PACKAGE_NAME}-targets)
set(HELLO_CONFIG_FILENAME ${HELLO_PACKAGE_NAME}-config.cmake)
set(HELLO_CONFIGVERSION_FILENAME ${HELLO_PACKAGE_NAME}-config-version.cmake)
set(HELLO_CMAKE_DIR cmake)

add_subdirectory(src)

# generate config file
configure_file(
	"${HELLO_CMAKE_DIR}/${HELLO_CONFIG_FILENAME}.in"
	"${HELLO_CMAKE_DIR}/${HELLO_CONFIG_FILENAME}"
	@ONLY
)

include(CMakePackageConfigHelpers)
write_basic_package_version_file("${HELLO_CMAKE_DIR}/${HELLO_CONFIGVERSION_FILENAME}"
	COMPATIBILITY SameMajorVersion
)

# install config and config-version files
install(FILES
	"${PROJECT_BINARY_DIR}/${HELLO_CMAKE_DIR}/${HELLO_CONFIG_FILENAME}"
	"${PROJECT_BINARY_DIR}/${HELLO_CMAKE_DIR}/${HELLO_CONFIGVERSION_FILENAME}"
	DESTINATION "lib/${HELLO_CMAKE_DIR}/${HELLO_PACKAGE_NAME}"
)
# export targets from an installation tree
install(EXPORT ${HELLO_EXPORT_NAME}
	NAMESPACE "${PROJECT_NAME}::"
	DESTINATION "lib/${HELLO_CMAKE_DIR}/${HELLO_PACKAGE_NAME}"
)

# export targets from a build tree
export(EXPORT ${HELLO_EXPORT_NAME} NAMESPACE "${PROJECT_NAME}::" FILE "${HELLO_CMAKE_DIR}/${HELLO_EXPORT_NAME}.cmake")

set_property(GLOBAL PROPERTY AUTOGEN_SOURCE_GROUP "Generated Files")
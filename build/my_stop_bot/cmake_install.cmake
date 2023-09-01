# Install script for directory: /home/shriram/Desktop/ros2_practice/src/my_stop_bot

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/shriram/Desktop/ros2_practice/install/my_stop_bot")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot" TYPE EXECUTABLE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/stop_bot")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot"
         OLD_RPATH "/opt/ros/humble/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/my_stop_bot/stop_bot")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/my_stop_bot")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/my_stop_bot")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot/environment" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot/environment" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/local_setup.bash")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/local_setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_environment_hooks/package.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_index/share/ament_index/resource_index/packages/my_stop_bot")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot/cmake" TYPE FILE FILES
    "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_core/my_stop_botConfig.cmake"
    "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/ament_cmake_core/my_stop_botConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/my_stop_bot" TYPE FILE FILES "/home/shriram/Desktop/ros2_practice/src/my_stop_bot/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/shriram/Desktop/ros2_practice/build/my_stop_bot/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")

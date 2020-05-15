{
  'variables': {
    'target_arch%': '<!(node preinstall.js --print-arch)>'
  },
  'targets': [
    {
      'target_name': 'sodium',
      'conditions': [
        ['OS == "android" or OS == "ios"', {
          'sources': [
            'binding.c'
          ],
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-g',
              '-O3',
              '-Wall',
            ]
          },
          'cflags': [
            '-g',
            '-O3',
            '-Wall',
          ],
        }],
        ['OS == "android"', {
          'include_dirs' : [
            'libsodium/src/libsodium/include'
          ],
          'libraries': [
            '<(module_root_dir)/lib/android-<(target_arch)/libsodium.so',
          ],
          'link_settings': {
            'libraries': [
              '-Wl,--enable-new-dtags',
              '-Wl,-rpath=\\$$ORIGIN'
            ]
          },
          'copies': [{
            'files': [
              '<(module_root_dir)/lib/android-<(target_arch)/libsodium.so',
            ],
            'destination': '<(PRODUCT_DIR)/',
          }],
        }],
        ['OS == "ios"', {
          'include_dirs' : [
            'libsodium/src/libsodium-ios/include'
          ],
          'libraries': [
            '<(module_root_dir)/lib/ios/libsodium.so',
          ],
          'copies': [{
            'files': [
              '<(module_root_dir)/lib/ios/libsodium.so',
            ],
            'destination': '<(PRODUCT_DIR)/',
          }],
        }],
      ]
    }
  ]
}

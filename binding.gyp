{
  'targets' : [
	  {
	    'target_name' : 'window_http_sync',
	    'conditions': [
	      ['"<!(echo $LUMIN)"=="1"', {
			    'sources' : [
		  	    'curllib.cc',
			    ],
			    'library_dirs': [
		        "<!(node -e \"console.log(require.resolve('libcurl.a').slice(0, -9) + '/lib')\")",
		      ],
			    'libraries' : [
			      '-lcurl',
			    ],
			    'include_dirs': [
				    "<!(node -e \"require('nan')\")",
				    "<!(node -e \"console.log(require.resolve('libcurl.a').slice(0, -9) + '/include')\")",
			    ],
          'defines': ['LUMIN'],
			  }],
			],
    },
  ]
}

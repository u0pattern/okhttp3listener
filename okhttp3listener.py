import frida, sys, argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="[+] okhttp3listener [+]")
	parser.add_argument('-a', required=True, default=None, help='Enter the App name')
	args = vars(parser.parse_args())
	if len(sys.argv) == 1:
		sys.exit("[!] Usage: python "+__file__+".py -a com.test.myApp [!]")
	js = """
		setImmediate(function() {
			console.log("\\n [*] Waiting for Requests");
			Java.perform(function () {
				var okhttp = Java.use("okhttp3.OkHttpClient");
				okhttp.newCall.implementation = function (request) {
					result = this.newCall(request);
					console.log(request.toString());
					return result;
				};
			});
		});
	"""
	process = frida.get_usb_device().attach([args['a'])
	script = process.create_script(js)
	script.load()
	sys.stdin.read()

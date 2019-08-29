Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: D:/Python/2019-8-8-异常2.py =====================
请输入需要打开的文件README
Traceback (most recent call last):
  File "D:/Python/2019-8-8-异常2.py", line 2, in <module>
    f = open(file_name)
FileNotFoundError: [Errno 2] No such file or directory: 'README'
>>> README.txt
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    README.txt
NameError: name 'README' is not defined
>>> 
===================== RESTART: D:/Python/2019-8-8-异常2.py =====================
请输入需要打开的文件README.txt
Traceback (most recent call last):
  File "D:/Python/2019-8-8-异常2.py", line 2, in <module>
    f = open(file_name)
FileNotFoundError: [Errno 2] No such file or directory: 'README.txt'
>>> 
===================== RESTART: D:/Python/2019-8-8-异常2.py =====================
请输入需要打开的文件NEWS.txt
文件的内容是
+++++++++++

Python News

+++++++++++



What's New in Python 3.7.4 final?

=================================



*Release date: 2019-07-08*



Core and Builtins

-----------------



- bpo-37500: Due to unintended side effects, revert the change introduced by

  :issue:`1875` in 3.7.4rc1 to check for syntax errors in dead conditional

  code blocks.



Documentation

-------------



- bpo-37149: Replace the dead link to the Tkinter 8.5 reference by John

  Shipman, New Mexico Tech, with a link to the archive.org copy.





What's New in Python 3.7.4 release candidate 2?

===============================================



*Release date: 2019-07-02*



Security

--------



- bpo-37463: ssl.match_hostname() no longer accepts IPv4 addresses with

  additional text after the address and only quad-dotted notation without

  trailing whitespaces. Some inet_aton() implementations ignore whitespace

  and all data after whitespace, e.g. '127.0.0.1 whatever'.



Core and Builtins

-----------------



- bpo-24214: Improved support of the surrogatepass error handler in the

  UTF-8 and UTF-16 incremental decoders.



Library

-------



- bpo-37440: http.client now enables TLS 1.3 post-handshake authentication

  for default context or if a cert_file is passed to HTTPSConnection.



- bpo-37437: Update vendorized expat version to 2.2.7.



- bpo-37428: SSLContext.post_handshake_auth = True no longer sets

  SSL_VERIFY_POST_HANDSHAKE verify flag for client connections. Although the

  option is documented as ignored for clients, OpenSSL implicitly enables

  cert chain validation when the flag is set.



- bpo-32627: Fix compile error when ``_uuid`` headers conflicting included.



Windows

-------



- bpo-37369: Fixes path for :data:`sys.executable` when running from the

  Microsoft Store.



- bpo-35360: Update Windows builds to use SQLite 3.28.0.



macOS

-----



- bpo-34602: Avoid test suite failures on macOS by no longer calling

  resource.setrlimit to increase the process stack size limit at runtime.

  The runtime change is no longer needed since the interpreter is being

  built with a larger default stack size.





What's New in Python 3.7.4 release candidate 1?

===============================================



*Release date: 2019-06-18*



Security

--------



- bpo-35907: CVE-2019-9948: Avoid file reading by disallowing

  ``local-file://`` and ``local_file://`` URL schemes in

  ``URLopener().open()`` and ``URLopener().retrieve()`` of

  :mod:`urllib.request`.



- bpo-36742: Fixes mishandling of pre-normalization characters in

  urlsplit().



- bpo-30458: Address CVE-2019-9740 by disallowing URL paths with embedded

  whitespace or control characters through into the underlying http client

  request.  Such potentially malicious header injection URLs now cause an

  http.client.InvalidURL exception to be raised.



- bpo-33529: Prevent fold function used in email header encoding from

  entering infinite loop when there are too many non-ASCII characters in a

  header.



- bpo-35755: :func:`shutil.which` now uses ``os.confstr("CS_PATH")`` if

  available and if the :envvar:`PATH` environment variable is not set.

  Remove also the current directory from :data:`posixpath.defpath`. On Unix,

  :func:`shutil.which` and the :mod:`subprocess` module no longer search the

  executable in the current directory if the :envvar:`PATH` environment

  variable is not set.



Core and Builtins

-----------------



- bpo-37269: Fix a bug in the peephole optimizer that was not treating

  correctly constant conditions with binary operators. Patch by Pablo

  Galindo.



- bpo-37219: Remove errorneous optimization for empty set differences.



- bpo-26423: Fix possible overflow in ``wrap_lenfunc()`` when ``sizeof(long)

  < sizeof(Py_ssize_t)`` (e.g., 64-bit Windows).



- bpo-36829: :c:func:`PyErr_WriteUnraisable` now displays the exception even

  if displaying the traceback failed. Moreover, hold a strong reference to

  :data:`sys.stderr` while using it. Document that an exception must be set

  when calling :c:func:`PyErr_WriteUnraisable`.



- bpo-36907: Fix a crash when calling a C function with a keyword dict

  (``f(**kwargs)``) and changing the dict ``kwargs`` while that function is

  running.



- bpo-36946: Fix possible signed integer overflow when handling slices.



- bpo-27987: ``PyGC_Head`` structure is aligned to ``long double``.  This is

  needed to ensure GC-ed objects are aligned properly.  Patch by Inada

  Naoki.



- bpo-1875: A :exc:`SyntaxError` is now raised if a code blocks that will be

  optimized away (e.g. if conditions that are always false) contains syntax

  errors. Patch by Pablo Galindo. (Reverted in 3.7.4 final by

  :issue:`37500`.)



- bpo-28866: Avoid caching attributes of classes which type defines mro() to

  avoid a hard cache invalidation problem.



- bpo-27639: Correct return type for UserList slicing operations. Patch by

  Michael Blahay, Erick Cervantes, and vaultah



- bpo-32849: Fix Python Initialization code on FreeBSD to detect properly

  when stdin file descriptor (fd 0) is invalid.



- bpo-27987: pymalloc returns memory blocks aligned by 16 bytes, instead of

  8 bytes, on 64-bit platforms to conform x86-64 ABI. Recent compilers

  assume this alignment more often. Patch by Inada Naoki.



- bpo-36504: Fix signed integer overflow in _ctypes.c's

  ``PyCArrayType_new()``.



- bpo-20844: Fix running script with encoding cookie and LF line ending may

  fail on Windows.



- bpo-24214: Fixed support of the surrogatepass error handler in the UTF-8

  incremental decoder.



- bpo-36459: Fix a possible double ``PyMem_FREE()`` due to tokenizer.c's

  ``tok_nextc()``.



- bpo-36433: Fixed TypeError message in classmethoddescr_call.



- bpo-36430: Fix a possible reference leak in :func:`itertools.count`.



- bpo-36440: Include node names in ``ParserError`` messages, instead of

  numeric IDs. Patch by A. Skrobov.



- bpo-36421: Fix a possible double decref in _ctypes.c's

  ``PyCArrayType_new()``.



- bpo-36256: Fix bug in parsermodule when parsing a state in a DFA that has

  two or more arcs with labels of the same type. Patch by Pablo Galindo.



- bpo-36236: At Python initialization, the current directory is no longer

  prepended to :data:`sys.path` if it has been removed.



- bpo-36262: Fix an unlikely memory leak on conversion from string to float

  in the function ``_Py_dg_strtod()`` used by ``float(str)``,

  ``complex(str)``, :func:`pickle.load`, :func:`marshal.load`, etc.



- bpo-36218: Fix a segfault occuring when sorting a list of heterogeneous

  values. Patch contributed by R茅mi Lapeyre and Elliot Gorokhovsky.



- bpo-36035: Added fix for broken symlinks in combination with pathlib



- bpo-18372: Add missing :c:func:`PyObject_GC_Track` calls in the

  :mod:`pickle` module. Patch by Zackery Spytz.



- bpo-34408: Prevent a null pointer dereference and resource leakage in

  ``PyInterpreterState_New()``.



Library

-------



- bpo-37280: Use threadpool for reading from file for sendfile fallback

  mode.



- bpo-37279: Fix asyncio sendfile support when sendfile sends extra data in

  fallback mode.



- bpo-19865: :func:`ctypes.create_unicode_buffer()` now also supports

  non-BMP characters on platforms with 16-bit :c:type:`wchar_t` (for

  example, Windows and AIX).



- bpo-35922: Fix :meth:`RobotFileParser.crawl_delay` and

  :meth:`RobotFileParser.request_rate` to return ``None`` rather than raise

  :exc:`AttributeError` when no relevant rule is defined in the robots.txt

  file.  Patch by R茅mi Lapeyre.



- bpo-36607: Eliminate :exc:`RuntimeError` raised by

  :func:`asyncio.all_tasks()` if internal tasks weak set is changed by

  another thread during iteration.



- bpo-36402: Fix a race condition at Python shutdown when waiting for

  threads. Wait until the Python thread state of all non-daemon threads get

  deleted (join all non-daemon threads), rather than just wait until

  non-daemon Python threads complete.



- bpo-34886: Fix an unintended ValueError from :func:`subprocess.run` when

  checking for conflicting `input` and `stdin` or `capture_output` and

  `stdout` or `stderr` args when they were explicitly provided but with

  `None` values within a passed in `**kwargs` dict rather than as passed

  directly by name. Patch contributed by R茅mi Lapeyre.



- bpo-37173: The exception message for ``inspect.getfile()`` now correctly

  reports the passed class rather than the builtins module.



- bpo-12639: :meth:`msilib.Directory.start_component()` no longer fails if

  *keyfile* is not ``None``.



- bpo-36520: Lengthy email headers with UTF-8 characters are now properly

  encoded when they are folded. Patch by Jeffrey Kintscher.



- bpo-37054: Fix destructor :class:`_pyio.BytesIO` and

  :class:`_pyio.TextIOWrapper`: initialize their ``_buffer`` attribute as

  soon as possible (in the class body), because it's used by ``__del__()``

  which calls ``close()``.



- bpo-30835: Fixed a bug in email parsing where a message with invalid bytes

  in content-transfer-encoding of a multipart message can cause an

  AttributeError. Patch by Andrew Donnellan.



- bpo-37035: Don't log OSError based exceptions if a fatal error has

  occurred in asyncio transport. Peer can generate almost any OSError, user

  cannot avoid these exceptions by fixing own code. Errors are still

  propagated to user code, it's just logging them is pointless and pollute

  asyncio logs.



- bpo-37008: Add support for calling :func:`next` with the mock resulting

  from :func:`unittest.mock.mock_open`



- bpo-27737: Allow whitespace only header encoding in ``email.header`` - by

  Batuhan Taskaya



- bpo-36969: PDB command `args` now  display keyword only arguments. Patch

  contributed by R茅mi Lapeyre.



- bpo-36983: Add missing names to ``typing.__all__``: ``ChainMap``,

  ``ForwardRef``, ``OrderedDict`` - by Anthony Sottile.



- bpo-21315: Email headers containing RFC2047 encoded words are parsed

  despite the missing whitespace, and a defect registered. Also missing

  trailing whitespace after encoded words is now registered as a defect.



- bpo-33524: Fix the folding of email header when the max_line_length is 0

  or None and the header contains non-ascii characters.  Contributed by

  Licht Takeuchi (@Licht-T).



- bpo-24564: :func:`shutil.copystat` now ignores :const:`errno.EINVAL` on

  :func:`os.setxattr` which may occur when copying files on filesystems

  without extended attributes support.



  Original patch by Giampaolo Rodola, updated by Ying Wang.



- bpo-36845: Added validation of integer prefixes to the construction of IP

  networks and interfaces in the ipaddress module.



- bpo-35545: Fix asyncio discarding IPv6 scopes when ensuring hostname

  resolutions internally



- bpo-35070: posix.getgrouplist() now works correctly when the user belongs

  to NGROUPS_MAX supplemental groups. Patch by Jeffrey Kintscher.



- bpo-24538: In `shutil.copystat()`, first copy extended file attributes and

  then file permissions, since extended attributes can only be set on the

  destination while it is still writeable.



- bpo-33110: Handle exceptions raised by functions added by

  concurrent.futures add_done_callback correctly when the Future has already

  completed.



- bpo-26903: Limit `max_workers` in `ProcessPoolExecutor` to 61 to work

  around a WaitForMultipleObjects limitation.



- bpo-36813: Fix :class:`~logging.handlers.QueueListener` to call

  ``queue.task_done()`` upon stopping. Patch by Bar Harel.



- bpo-36734: Fix compilation of ``faulthandler.c`` on HP-UX. Initialize

  ``stack_t current_stack`` to zero using ``memset()``.



- bpo-29183: Fix double exceptions in :class:`wsgiref.handlers.BaseHandler`

  by calling its :meth:`~wsgiref.handlers.BaseHandler.close` method only

  when no exception is raised.



- bpo-36650: The C version of functools.lru_cache() was treating calls with

  an empty ``**kwargs`` dictionary as being distinct from calls with no

  keywords at all. This did not result in an incorrect answer, but it did

  trigger an unexpected cache miss.



- bpo-28552: Fix :mod:`distutils.sysconfig` if :data:`sys.executable` is

  ``None`` or an empty string: use :func:`os.getcwd` to initialize

  ``project_base``.  Fix also the distutils build command: don't use

  :data:`sys.executable` if it is ``None`` or an empty string.



- bpo-35755: :func:`shutil.which` and

  :func:`distutils.spawn.find_executable` now use ``os.confstr("CS_PATH")``

  if available instead of :data:`os.defpath`, if the ``PATH`` environment

  variable is not set. Moreover, don't use ``os.confstr("CS_PATH")`` nor

  :data:`os.defpath` if the ``PATH`` environment variable is set to an empty

  string.



- bpo-36613: Fix :mod:`asyncio` wait() not removing callback if exception



- bpo-36598: Fix ``isinstance`` check for Mock objects with spec when the

  code is executed under tracing. Patch by Karthikeyan Singaravelan.



- bpo-36533: Reinitialize logging.Handler locks in forked child processes

  instead of attempting to acquire them all in the parent before forking

  only to be released in the child process.  The acquire/release pattern was

  leading to deadlocks in code that has implemented any form of chained

  logging handlers that depend upon one another as the lock acquision order

  cannot be guaranteed.



- bpo-36522: If *debuglevel* is set to >0 in :mod:`http.client`, print all

  values for headers with multiple values for the same header name. Patch by

  Matt Houglum.



- bpo-36492: Arbitrary keyword arguments (even with names "self" and "func")

  can now be passed to some functions which should accept arbitrary keyword

  arguments and pass them to other function (for example partialmethod(),

  TestCase.addCleanup() and Profile.runcall()) if the required arguments are

  passed as positional arguments.



- bpo-36434: Errors during writing to a ZIP file no longer prevent to

  properly close it.



- bpo-34745: Fix :mod:`asyncio` ssl memory issues caused by circular

  references



- bpo-36321: collections.namedtuple() misspelled the name of an attribute.

  To be consistent with typing.NamedTuple, the attribute name should have

  been "_field_defaults" instead of "_fields_defaults".  For backwards

  compatibility, both spellings are now created.  The misspelled version may

  be removed in the future.



- bpo-36272: :mod:`logging` does not silently ignore RecursionError anymore.

  Patch contributed by R茅mi Lapeyre.



- bpo-36235: Fix ``CFLAGS`` in ``customize_compiler()`` of

  ``distutils.sysconfig``: when the ``CFLAGS`` environment variable is

  defined, don't override ``CFLAGS`` variable with the ``OPT`` variable

  anymore. Initial patch written by David Malcolm.



- bpo-35125: Asyncio: Remove inner callback on outer cancellation in shield



- bpo-35802: Clean up code which checked presence of ``os.stat`` /

  ``os.lstat`` / ``os.chmod`` which are always present.  Patch by Anthony

  Sottile.



- bpo-23078: Add support for :func:`classmethod` and :func:`staticmethod` to

  :func:`unittest.mock.create_autospec`.  Initial patch by Felipe Ochoa.



- bpo-35721: Fix :meth:`asyncio.SelectorEventLoop.subprocess_exec()` leaks

  file descriptors if ``Popen`` fails and called with

  ``stdin=subprocess.PIPE``. Patch by Niklas Fiekas.



- bpo-35726: QueueHandler.prepare() now makes a copy of the record before

  modifying and enqueueing it, to avoid affecting other handlers in the

  chain.



- bpo-31855: :func:`unittest.mock.mock_open` results now respects the

  argument of read([size]). Patch contributed by R茅mi Lapeyre.



- bpo-35082: Don't return deleted attributes when calling dir on a

  :class:`unittest.mock.Mock`.



- bpo-34547: :class:`wsgiref.handlers.BaseHandler` now handles abrupt client

  connection terminations gracefully. Patch by Petter Strandmark.



- bpo-34424: Fix serialization of messages containing encoded strings when

  the policy.linesep is set to a multi-character string. Patch by Jens

  Troeger.



- bpo-33361: Fix a bug in :class:`codecs.StreamRecoder` where seeking might

  leave old data in a buffer and break subsequent read calls. Patch by Ammar

  Askar.



- bpo-31922: :meth:`asyncio.AbstractEventLoop.create_datagram_endpoint`: Do

  not connect UDP socket when broadcast is allowed. This allows to receive

  replies after a UDP broadcast.



- bpo-22102: Added support for ZIP files with disks set to 0. Such files are

  commonly created by builtin tools on Windows when use ZIP64 extension.

  Patch by Francisco Facioni.



- bpo-27141: Added a ``__copy__()`` to ``collections.UserList`` and

  ``collections.UserDict`` in order to correctly implement shallow copying

  of the objects. Patch by Bar Harel.



- bpo-31829: ``\r``, ``\0`` and ``\x1a`` (end-of-file on Windows) are now

  escaped in protocol 0 pickles of Unicode strings. This allows to load them

  without loss from files open in text mode in Python 2.



- bpo-31292: Fix ``setup.py check --restructuredtext`` for files containing

  ``include`` directives.



- bpo-23395: ``_thread.interrupt_main()`` now avoids setting the Python

  error status if the ``SIGINT`` signal is ignored or not handled by Python.



Documentation

-------------



- bpo-34903: Documented that in :meth:`datetime.datetime.strptime()`, the

  leading zero in some two-digit formats is optional. Patch by Mike Gleen.



- bpo-36984: Improve version added references in ``typing`` module - by

  Anthony Sottile.



- bpo-36868: What's new now mentions SSLContext.hostname_checks_common_name

  instead of SSLContext.host_flags.



- bpo-36783: Added C API Documentation for Time_FromTimeAndFold and

  PyDateTime_FromDateAndTimeAndFold as per PEP 495. Patch by Edison

  Abahurire.



- bpo-30840: Document relative imports



- bpo-36523: Add docstring for io.IOBase.writelines().



- bpo-36425: New documentation translation: `Simplified Chinese

  <https://docs.python.org/zh-cn/>`_.



- bpo-36157: Added Documention for  PyInterpreterState_Main().



- bpo-36138: Improve documentation about converting datetime.timedelta to

  scalars.



- bpo-22865: Add detail to the documentation on the `pty.spawn` function.



- bpo-35581: @typing.type_check_only now allows type stubs to mark functions

  and classes not available during runtime.



- bpo-35564: Explicitly set master_doc variable in conf.py for compliance

  with Sphinx 2.0



- bpo-10536: Enhance the gettext docs. Patch by 脡ric Araujo



- bpo-32995: Added the context variable in glossary.



- bpo-33832: Add glossary entry for 'magic method'.



- bpo-33482: Make `codecs.StreamRecoder.writelines` take a list of bytes.



- bpo-25735: Added documentation for func factorial to indicate that returns

  integer values



Tests

-----



- bpo-35998: Avoid TimeoutError in test_asyncio: test_start_tls_server_1()



- bpo-37153: ``test_venv.test_mutiprocessing()`` now explicitly calls

  ``pool.terminate()`` to wait until the pool completes.



- bpo-37081: Test with OpenSSL 1.1.1c



- bpo-36915: The main regrtest process now always removes all temporary

  directories of worker processes even if they crash or if they are killed

  on KeyboardInterrupt (CTRL+c).



- bpo-36719: "python3 -m test -jN ..." now continues the execution of next

  tests when a worker process crash (CHILD_ERROR state). Previously, the

  test suite stopped immediately. Use --failfast to stop at the first error.



- bpo-36816: Update Lib/test/selfsigned_pythontestdotnet.pem to match

  self-signed.pythontest.net's new TLS certificate.



- bpo-35925: Skip httplib and nntplib networking tests when they would

  otherwise fail due to a modern OS or distro with a default OpenSSL policy

  of rejecting connections to servers with weak certificates.



- bpo-36719: regrtest now always detects uncollectable objects. Previously,

  the check was only enabled by ``--findleaks``. The check now also works

  with ``-jN/--multiprocess N``. ``--findleaks`` becomes a deprecated alias

  to ``--fail-env-changed``.



- bpo-36725: When using mulitprocessing mode (-jN), regrtest now better

  reports errors if a worker process fails, and it exits immediately on a

  worker thread failure or when interrupted.



- bpo-36454: Change test_time.test_monotonic() to test only the lower bound

  of elapsed time after a sleep command rather than the upper bound. This

  prevents unnecessary test failures on slow buildbots. Patch by Victor

  Stinner.



- bpo-36629: Fix ``test_imap4_host_default_value()`` of ``test_imaplib``:

  catch also :data:`errno.ENETUNREACH` error.



- bpo-36611: Fix ``test_sys.test_getallocatedblocks()`` when

  :mod:`tracemalloc` is enabled.



- bpo-36560: Fix reference leak hunting in regrtest: compute also deltas (of

  reference count, allocated memory blocks, file descriptor count) during

  warmup, to ensure that everything is initialized before starting to hunt

  reference leaks.



- bpo-36565: Fix reference hunting (``python3 -m test -R 3:3``) when Python

  has no built-in abc module.



- bpo-36436: Fix ``_testcapi.pymem_buffer_overflow()``: handle memory

  allocation failure.



Build

-----



- bpo-36605: ``make tags`` and ``make TAGS`` now also parse

  ``Modules/_io/*.c`` and ``Modules/_io/*.h``.



- bpo-36508: ``python-config --ldflags`` no longer includes flags of the

  ``LINKFORSHARED`` variable. The ``LINKFORSHARED`` variable must only be

  used to build executables.



Windows

-------



- bpo-34631: Updated OpenSSL to 1.1.1c in Windows installer



- bpo-37267: On Windows, :func:`os.dup` no longer creates an inheritable fd

  when handling a character file.



- bpo-36779: Ensure ``time.tzname`` is correct on Windows when the active

  code page is set to CP_UTF7 or CP_UTF8.



- bpo-36965: include of STATUS_CONTROL_C_EXIT without depending on MSC

  compiler



- bpo-36649: Remove trailing spaces for registry keys when installed via the

  Store.



- bpo-34144: Fixed activate.bat to correctly update codepage when chcp.com

  returns dots in output. Patch by Lorenz Mende.



- bpo-35941: enum_certificates function of the ssl module now returns

  certificates from all available certificate stores inside windows in a

  query instead of returning only certificates from the system wide

  certificate store. This includes certificates from these certificate

  stores: local machine, local machine enterprise, local machine group

  policy, current user, current user group policy, services, users.

  ssl.enum_crls() function is changed in the same way to return all

  certificate revocation lists inside the windows certificate revocation

  list stores.



- bpo-36441: Fixes creating a venv when debug binaries are installed.



- bpo-36312: Fixed decoders for the following code pages: 50220, 50221,

  50222, 50225, 50227, 50229, 57002 through 57011, 65000 and 42.



- bpo-36010: Add the venv standard library module to the nuget distribution

  for Windows.



- bpo-34060: Report system load when running test suite on Windows. Patch by

  Ammar Askar. Based on prior work by Jeremy Kloth.



macOS

-----



- bpo-35360: Update macOS installer to use SQLite 3.28.0.



- bpo-34631: Updated OpenSSL to 1.1.1c in macOS installer.



- bpo-36231: Support building Python on macOS without /usr/include

  installed. As of macOS 10.14, system header files are only available

  within an SDK provided by either the Command Line Tools or the Xcode app.



- bpo-34602: Avoid failures setting macOS stack resource limit with

  resource.setrlimit. This reverts an earlier fix for bpo-18075 which forced

  a non-default stack size when building the interpreter executable on

  macOS.



IDLE

----



- bpo-37321: Both subprocess connection error messages now refer to the

  'Startup failure' section of the IDLE doc.



- bpo-37177: Properly 'attach' search dialogs to their main window so that

  they behave like other dialogs and do not get hidden behind their main

  window.



- bpo-37039: Adjust "Zoom Height" to individual screens by momemtarily

  maximizing the window on first use with a particular screen.  Changing

  screen settings may invalidate the saved height.  While a window is

  maximized, "Zoom Height" has no effect.



- bpo-35763: Make calltip reminder about '/' meaning positional-only less

  obtrusive by only adding it when there is room on the first line.



- bpo-5680: Add 'Run... Customized' to the Run menu to run a module with

  customized settings.  Any 'command line arguments' entered are added to

  sys.argv. One can suppress the normal Shell main module restart.



- bpo-35610: Replace now redundant .context_use_ps1 with .prompt_last_line.

  This finishes change started in bpo-31858.



- bpo-37038: Make idlelib.run runnable; add test clause.



- bpo-36958: Print any argument other than None or int passed to SystemExit

  or sys.exit().



- bpo-13102: When saving a file, call os.fsync() so bits are flushed to e.g.

  USB drive.



- bpo-36429: Fix starting IDLE with pyshell. Add idlelib.pyshell alias at

  top; remove pyshell alias at bottom. Remove obsolete __name__=='__main__'

  command.



- bpo-36405: Use dict unpacking in idlelib.



- bpo-36396: Remove fgBg param of idlelib.config.GetHighlight(). This param

  was only used twice and changed the return type.



- bpo-23205: For the grep module, add tests for findfiles, refactor

  findfiles to be a module-level function, and refactor findfiles to use

  os.walk.



- bpo-23216: Add docstrings to IDLE search modules.



- bpo-30348: Increase test coverage of idlelib.autocomplete by 30%.



- bpo-32411: In browser.py, remove extraneous sorting by line number since

  dictionary was created in line number order.



Tools/Demos

-----------



- bpo-14546: Fix the argument handling in Tools/scripts/lll.py.



- bpo-32217: Fix freeze script on Windows.



C API

-----



- bpo-28805: The :const:`METH_FASTCALL` calling convention has been

  documented.



- bpo-37170: Fix the cast on error in

  :c:func:`PyLong_AsUnsignedLongLongMask()`.



- bpo-36389: Change the value of ``CLEANBYTE``, ``DEADDYTE`` and

  ``FORBIDDENBYTE`` internal constants used by debug hooks on Python memory

  allocators (:c:func:`PyMem_SetupDebugHooks` function). Byte patterns

  ``0xCB``, ``0xDB`` and ``0xFB`` have been replaced with ``0xCD``, ``0xDD``

  and ``0xFD`` to use the same values than Windows CRT debug ``malloc()``

  and ``free()``.





What's New in Python 3.7.3 final?

=================================



*Release date: 2019-03-25*



There were no new changes in version 3.7.3.







What's New in Python 3.7.3 release candidate 1?

===============================================



*Release date: 2019-03-12*



Security

--------



- bpo-36216: Changes urlsplit() to raise ValueError when the URL contains

  characters that decompose under IDNA encoding (NFKC-normalization) into

  characters that affect how the URL is parsed.



- bpo-35746: [CVE-2019-5010] Fix a NULL pointer deref in ssl module. The

  cert parser did not handle CRL distribution points with empty DP or URI

  correctly. A malicious or buggy certificate can result into segfault.

  Vulnerability (TALOS-2018-0758) reported by Colin Read and Nicolas Edet of

  Cisco.



- bpo-35121: Don't send cookies of domain A without Domain attribute to

  domain B when domain A is a suffix match of domain B while using a

  cookiejar with :class:`http.cookiejar.DefaultCookiePolicy` policy. Patch

  by Karthikeyan Singaravelan.



Core and Builtins

-----------------



- bpo-35942: The error message emitted when returning invalid types from

  ``__fspath__`` in interfaces that allow passing :class:`~os.PathLike`

  objects has been improved and now it does explain the origin of the error.



- bpo-35992: Fix ``__class_getitem__()`` not being called on a class with a

  custom non-subscriptable metaclass.



- bpo-35991: Fix a potential double free in Modules/_randommodule.c.



- bpo-35961: Fix a crash in slice_richcompare(): use strong references

  rather than stolen references for the two temporary internal tuples.



- bpo-31506: Clarify the errors reported when ``object.__new__`` and

  ``object.__init__`` receive more than one argument. Contributed by Sanyam

  Khurana.



- bpo-35720: Fixed a minor memory leak in pymain_parse_cmdline_impl function

  in Modules/main.c



- bpo-35623: Fix a crash when sorting very long lists. Patch by Stephan

  Hohe.



- bpo-35214: clang Memory Sanitizer build instrumentation was added to work

  around false positives from posix, socket, time, test_io, and

  test_faulthandler.



- bpo-35560: Fix an assertion error in :func:`format` in debug build for

  floating point formatting with "n" format, zero padding and small width.

  Release build is not impacted. Patch by Karthikeyan Singaravelan.



- bpo-35552: Format characters ``%s`` and ``%V`` in

  :c:func:`PyUnicode_FromFormat` and ``%s`` in :c:func:`PyBytes_FromFormat`

  no longer read memory past the limit if *precision* is specified.



- bpo-35504: Fix segfaults and :exc:`SystemError`\ s when deleting certain

  attributes. Patch by Zackery Spytz.



- bpo-33989: Fix a possible crash in :meth:`list.sort` when sorting objects

  with ``ob_type->tp_richcompare == NULL``.  Patch by Zackery Spytz.



Library

-------



- bpo-35931: The :mod:`pdb` ``debug`` command now gracefully handles all

  exceptions.



- bpo-36251: Fix format strings used for stderrprinter and re.Match reprs.

  Patch by Stephan Hohe.



- bpo-35807: Update ensurepip to install pip 19.0.3 and setuptools 40.8.0.



- bpo-36179: Fix two unlikely reference leaks in _hashopenssl. The leaks

  only occur in out-of-memory cases.



- bpo-35178: Ensure custom :func:`warnings.formatwarning` function can

  receive `line` as positional argument. Based on patch by Tashrif Billah.



- bpo-36106: Resolve potential name clash with libm's sinpi(). Patch by

  Dmitrii Pasechnik.



- bpo-35512: :func:`unittest.mock.patch.dict` used as a decorator with

  string target resolves the target during function call instead of during

  decorator construction. Patch by Karthikeyan Singaravelan.



- bpo-36091: Clean up reference to async generator in Lib/types. Patch by

  Henry Chen.



- bpo-35899: Enum has been fixed to correctly handle empty strings and

  strings with non-Latin characters (ie. '伪', '讗') without crashing.

  Original patch contributed by Maxwell. Assisted by St茅phane Wirtel.



- bpo-35918: Removed broken ``has_key`` method from

  multiprocessing.managers.SyncManager.dict. Contributed by R茅mi Lapeyre.



- bpo-35960: Fix :func:`dataclasses.field` throwing away empty mapping

  objects passed as metadata.



- bpo-35847: RISC-V needed the CTYPES_PASS_BY_REF_HACK.  Fixes ctypes

  Structure test_pass_by_value.



- bpo-35780: Fix lru_cache() errors arising in recursive, reentrant, or

  multi-threaded code. These errors could result in orphan links and in the

  cache being trapped in a state with fewer than the specified maximum

  number of links. Fix handling of negative maxsize which should have been

  treated as zero. Fix errors in toggling the "full" status flag. Fix

  misordering of links when errors are encountered.  Sync-up the C code and

  pure Python code for the space saving path in functions with a single

  positional argument. In this common case, the space overhead of an lru

  cache entry is reduced by almost half.  Fix counting of cache misses. In

  error cases, the miss count was out of sync with the actual number of

  times the underlying user function was called.



- bpo-23846: :class:`asyncio.ProactorEventLoop` now catches and logs send

  errors when the self-pipe is full.



- bpo-34323: :mod:`asyncio`: Enhance ``IocpProactor.close()`` log: wait 1

  second before the first log, then log every second. Log also the number of

  seconds since ``close()`` was called.



- bpo-34294: re module, fix wrong capturing groups in rare cases.

  :func:`re.search`, :func:`re.findall`, :func:`re.sub` and other functions

  that scan through string looking for a match, should reset capturing

  groups between two match attempts. Patch by Ma Lin.



- bpo-35717: Fix KeyError exception raised when using enums and compile.

  Patch contributed by R茅mi Lapeyre.



- bpo-35699: Fixed detection of Visual Studio Build Tools 2017 in distutils



- bpo-32710: Fix memory leaks in asyncio ProactorEventLoop on overlapped

  operation failure.



- bpo-32710: Fix a memory leak in asyncio in the ProactorEventLoop when

  ``ReadFile()`` or ``WSASend()`` overlapped operation fail immediately:

  release the internal buffer.



- bpo-35682: Fix ``asyncio.ProactorEventLoop.sendfile()``: don't attempt to

  set the result of an internal future if it's already done.



- bpo-35283: Add a pending deprecated warning for the

  :meth:`threading.Thread.isAlive` method. Patch by Dong-hee Na.



- bpo-35643: Fixed a SyntaxWarning: invalid escape sequence in

  Modules/_sha3/cleanup.py. Patch by Micka毛l Schoentgen.



- bpo-35615: :mod:`weakref`: Fix a RuntimeError when copying a

  WeakKeyDictionary or a WeakValueDictionary, due to some keys or values

  disappearing while iterating.



- bpo-28503: The `crypt` module now internally uses the `crypt_r()` library

  function instead of `crypt()` when available.



- bpo-35121: Don't set cookie for a request when the request path is a

  prefix match of the cookie's path attribute but doesn't end with "/".

  Patch by Karthikeyan Singaravelan.



- bpo-35585: Speed-up building enums by value, e.g. http.HTTPStatus(200).



- bpo-21478: Calls to a child function created with

  :func:`unittest.mock.create_autospec` should propagate to the parent.

  Patch by Karthikeyan Singaravelan.



- bpo-35513: :class:`~unittest.runner.TextTestRunner` of

  :mod:`unittest.runner` now uses :func:`time.perf_counter` rather than

  :func:`time.time` to measure the execution time of a test:

  :func:`time.time` can go backwards, whereas :func:`time.perf_counter` is

  monotonic.



- bpo-35502: Fixed reference leaks in

  :class:`xml.etree.ElementTree.TreeBuilder` in case of unfinished building

  of the tree (in particular when an error was raised during parsing XML).



- bpo-31446: Copy command line that was passed to CreateProcessW since this

  function can change the content of the input buffer.



- bpo-20239: Allow repeated assignment deletion of

  :class:`unittest.mock.Mock` attributes. Patch by Pablo Galindo.



- bpo-17185: Set ``__signature__`` on mock for :mod:`inspect` to get

  signature. Patch by Karthikeyan Singaravelan.



- bpo-10496: :func:`~distutils.utils.check_environ` of

  :mod:`distutils.utils` now catches :exc:`KeyError` on calling

  :func:`pwd.getpwuid`: don't create the ``HOME`` environment variable in

  this case.



- bpo-35066: Previously, calling the strftime() method on a datetime object

  with a trailing '%' in the format string would result in an exception.

  However, this only occured when the datetime C module was being used; the

  python implementation did not match this behavior. Datetime is now PEP-399

  compliant, and will not throw an exception on a trailing '%'.



- bpo-24746: Avoid stripping trailing whitespace in doctest fancy diff.

  Orignial patch by R. David Murray & Jairo Trad. Enhanced by Sanyam

  Khurana.



- bpo-35198: Fix C++ extension compilation on AIX



- bpo-28441: On Cygwin and MinGW, ensure that ``sys.executable`` always

  includes the full filename in the path, including the ``.exe`` suffix

  (unless it is a symbolic link).



- bpo-34572: Fix C implementation of pickle.loads to use importlib's locking

  mechanisms, and thereby avoid using partially-loaded modules. Patch by Tim

  Burgess.



- bpo-33687: Fix the call to ``os.chmod()`` for ``uu.decode()`` if a mode is

  given or decoded. Patch by Timo Furrer.




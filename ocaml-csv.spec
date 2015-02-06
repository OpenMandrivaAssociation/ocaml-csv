%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library for reading and writing CSV files
Name:		ocaml-csv
Version:	1.3.3
Release:	2
License:	LGPLv2+
Group:		Development/Other
Url:		http://forge.ocamlcore.org/projects/csv/
Source0:	http://forge.ocamlcore.org/frs/download.php/1235/csv-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, quote-0 etc.

The library comes with a handy command line tool called csvtool for
handling CSV files from shell scripts.

%files
%doc README.txt AUTHORS.txt LICENSE.txt
%{_libdir}/ocaml/csv
%exclude %{_libdir}/ocaml/csv/*.a
%exclude %{_libdir}/ocaml/csv/*.cmxa
%exclude %{_libdir}/ocaml/csv/*.mli
%{_bindir}/csvtool

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc examples/
%doc tests/
%{_libdir}/ocaml/csv/*.a
%{_libdir}/ocaml/csv/*.cmxa
%{_libdir}/ocaml/csv/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n csv-%{version}

%build
ocaml setup.ml -configure --prefix %{_prefix} --destdir %{buildroot}
ocaml setup.ml -build
strip _build/examples/csvtool.native

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/site-lib/
mkdir -p $DESTDIR/%{_bindir}
ocaml setup.ml -install
cp _build/examples/csvtool.native %{buildroot}/%{_bindir}/csvtool

%check
ocaml setup.ml -test


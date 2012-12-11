Name:           ocaml-csv
Version:        1.1.7
Release:        %mkrel 3
Summary:        OCaml library for reading and writing CSV files

Group:          Development/Other
License:        LGPLv2+
URL:            http://merjis.com/developers/csv
Source0:        http://merjis.com/_file/ocaml-csv-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Patch0:         csv-extlib.patch
Patch1:         csv-install.patch

BuildRequires:  ocaml >= 3.10.1
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-extlib-devel
BuildRequires:  gawk


%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, quote-0 etc.

The library comes with a handy command line tool called csvtool for
handling CSV files from shell scripts.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p0
%patch1 -p1


%build
#make all
make csv.cma
make csvtool csv.cmxa
strip csvtool


%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
mkdir -p $OCAMLFIND_DESTDIR/site-lib/
mkdir -p $DESTDIR/%{_bindir}
make install BINDIR=%{_bindir}

# Create some documentation.
if [ ! -f README ]; then
  cat <<EOM > README
OCaml library for reading and writing CSV files.
For more information, see http://merjis.com/developers/csv .
This library is released under the GNU LGPL + OCaml linking exception.
EOM
fi


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/ocaml/csv
%exclude %{_libdir}/ocaml/csv/*.a
%exclude %{_libdir}/ocaml/csv/*.cmxa
%exclude %{_libdir}/ocaml/csv/*.cmx
%exclude %{_libdir}/ocaml/csv/*.mli
%{_bindir}/csvtool


%files devel
%defattr(-,root,root,-)
%doc README
%{_libdir}/ocaml/csv/*.a
%{_libdir}/ocaml/csv/*.cmxa
%{_libdir}/ocaml/csv/*.cmx
%{_libdir}/ocaml/csv/*.mli




%changelog
* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.7-3mdv2010.0
+ Revision: 390240
- rebuild

* Tue Feb 03 2009 Florent Monnier <blue_prawn@mandriva.org> 1.1.7-2mdv2010.0
+ Revision: 337139
- The initial RPM release was made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones

* Tue Jan 06 2009 Florent Monnier <blue_prawn@mandriva.org> 1.1.7-1mdv2009.1
+ Revision: 326204
- import ocaml-csv


* Sat Dec 20 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.1.7-1mdv
- Initial RPM release made from the fedora rpm .spec file (revision 1.9) by Richard W.M. Jones
# found there: http://cvs.fedoraproject.org/viewvc/devel/ocaml-csv/
# csv-extlib.patch : rev 1.1
# csv-install.patch : rev 1.2
# ocaml-csv.spec : rev 1.9

# TODO
# - rename spec, or package mysqldiff program as subpackage?
#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires mysql server and access to test_* tables)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MySQL
%define		pnam	Diff
Name:		mysqldiff
Summary:	Perl script which compares the table definitions of two MySQL databases
Version:	0.33
Release:	1.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f8e4af9eacd465814ce4071e9457272
URL:		http://adamspiers.org/computing/mysqldiff/
BuildRequires:	perl-Class-MakeMethods
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	mysql-client
%endif
Requires:	perl-Class-MakeMethods
Requires:	perl-%{pdir}-%{pnam}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqldiff is a Perl script front-end to the CPAN module MySQL::Diff
which compares the data structures (i.e. table definitions) of two
MySQL databases, and returns the differences as a sequence of MySQL
commands suitable for piping into mysql which will transform the
structure of the first database to be identical to that of the second
(c.f. diff and patch). Database structures can be compared whether
they are files containing table definitions or existing databases,
local or remote.

%package -n perl-%{pdir}-%{pnam}
Summary:	MySQL::Diff Perl module - comparing the table structure of two MySQL databases
Summary(pl):	Modu³ Perla MySQL::Diff - porównywanie struktury tabel dwóch baz danych MySQL
Group:		Development/Languages/Perl

%description  -n perl-%{pdir}-%{pnam}
MySQL::Diff is Perl module for comparing the table structure of two
MySQL databases.

%description -l pl
MySQL::Diff to modu³ Perla s³u¿±cy do porównywania struktury tabel
dwóch baz danych MySQL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install mysqldiff $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mysqldiff

%files -n perl-%{pdir}-%{pnam}
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/MySQL
%{perl_vendorlib}/MySQL/Database.pm
%{perl_vendorlib}/MySQL/Diff.pm
%{perl_vendorlib}/MySQL/Table.pm
%{perl_vendorlib}/MySQL/Utils.pm

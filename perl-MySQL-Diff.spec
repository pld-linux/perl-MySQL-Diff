#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires mysql server and access to test_* tables)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MySQL
%define		pnam	Diff
Summary:	MySQL::Diff Perl module - comparing the table structure of two MySQL databases
Summary(pl):	Modu³ Perla MySQL::Diff - porównywanie struktury tabel dwóch baz danych MySQL
Name:		perl-%{pdir}-%{pnam}
Version:	0.33
Release:	1
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
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

# mysqldiff binary is not installed somewhy by perl
install -d $RPM_BUILD_ROOT%{_bindir}
install mysqldiff $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mysqldiff
%dir %{perl_vendorlib}/MySQL
%{perl_vendorlib}/MySQL/Database.pm
%{perl_vendorlib}/MySQL/Diff.pm
%{perl_vendorlib}/MySQL/Table.pm
%{perl_vendorlib}/MySQL/Utils.pm

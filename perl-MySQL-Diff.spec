#
# NOTE: Tests require running mysql server and access to test_* tables
#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MySQL
%define		pnam	Diff
Summary:	MySQL-Diff perl module
Name:		perl-%{pdir}-%{pnam}
Version:	0.33
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://adamspiers.org/computing/mysqldiff/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Class-MakeMethods
%if %{with tests}
BuildRequires:	mysql-client
%endif
Requires:	perl-Class-MakeMethods
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL::Diff is Perl module for comparing the table structure of two MySQL
databases.

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

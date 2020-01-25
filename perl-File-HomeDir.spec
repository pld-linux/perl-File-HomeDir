#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	File
%define	pnam	HomeDir
Summary:	File::HomeDir - Find your home and other directories, on any platform
Summary(pl.UTF-8):	File::HomeDir - określanie katalogu domowego i innych katalogów na dowolnej platformie
Name:		perl-File-HomeDir
Version:	1.004
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2db6a961960baec790a896b99b46395d
URL:		http://search.cpan.org/dist/File-HomeDir/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Cwd) >= 3.12
BuildRequires:	perl(File::Path) >= 2.01
BuildRequires:	perl(File::Spec) >= 3.12
BuildRequires:	perl-File-Temp >= 0.19
BuildRequires:	perl-File-Which >= 0.05
BuildRequires:	perl-Test-Simple >= 0.47
%endif
Requires:	perl(Cwd) >= 3.12
Requires:	perl(File::Path) >= 2.01
Requires:	perl(File::Spec) >= 3.12
Requires:	perl-File-Temp >= 0.19
Requires:	perl-File-Which >= 0.05
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::HomeDir is a module for dealing with issues relating to the
location of directories that are "owned" by a user, primarily your
user, and to solve these issues consistently across a wide variety of
platforms.

%description -l pl.UTF-8
File::HomeDir to moduł do rozwiązywania kwestii związanych z
położeniem katalogów należących do użytkownika w sposób spójny dla
wielu platform.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/File/HomeDir.pm
%{perl_vendorlib}/File/HomeDir
%{_mandir}/man3/File::HomeDir*.3pm*

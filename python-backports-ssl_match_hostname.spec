%define		module_name	backports.ssl_match_hostname
Summary:	The ssl.match_hostname() function from Python 3
Summary(pl.UTF-8):	Funkcja ssl.match_hostname() z Pythona 3
Name:		python-backports-ssl_match_hostname
Version:	3.7.0.1
Release:	3
License:	PSF v2
Group:		Libraries/Python
# Source0Download: https://pypi.python.org/simple/backports.ssl-match-hostname/
Source0:	https://pypi.python.org/packages/source/b/backports.ssl_match_hostname/%{module_name}-%{version}.tar.gz
# Source0-md5:	32d2f593af01a046bec3d2f5181a420a
URL:		https://bitbucket.org/brandon/backports.ssl_match_hostname
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-backports >= 1.0-9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Secure Sockets layer is only actually secure if you check the
hostname in the certificate returned by the server to which you are
connecting, and verify that it matches to hostname that you are trying
to reach.

But the matching logic, defined in RFC2818, can be a bit tricky to
implement on your own. So the ssl package in the Standard Library of
Python 3.2 now includes a match_hostname() function for performing
this check instead of requiring every application to implement the
check separately.

This backport brings match_hostname() to users of earlier versions of
Python. The actual code inside comes from Python 3.7 with small
changes for portability.

%description -l pl.UTF-8
Warstwa bezpiecznych gniazd (Secure Sockets Layer) jest naprawdę
bezpieczna tylko jeśli sprawdza się nazwę hosta w certyfikacie
zwracanym przez serwer, z którym się łączy i weryfikuje, że zgadza się
ona z pożądaną nazwą hosta.

Ale logika dopasowująca, zdefiniowana w RFC2818, może być nietrywialna
do zaimplementowania samemu. Dlatego też pakiet ssl biblioteki
standardowej Pythona 3.2 zawiera teraz funkcję match_hostname(), która
wykonuje to sprawdzenie zamiast wymagania implementacji w każdej
aplikacji.

Ten backport udostępnia match_hostname() użytkownikom wcześniejszych
wersji Pythona. Sam kod pochodzi z Pythona 3.7 z niewielkimi zmianami
pod kątem przenośności.

%prep
%setup -qn %{module_name}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

# belongs to python-backports
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.py*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt
%{py_sitescriptdir}/backports/ssl_match_hostname
%{py_sitescriptdir}/backports.ssl_match_hostname-%{version}-py*.egg-info

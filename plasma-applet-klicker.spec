%define		oname	klicker
Name:		plasma-applet-%{oname}
Summary:	Klicker is an icon application launcher, with zoomK
Version:	0.1.1
Release:	%mkrel 1
Url:		http://kde-look.org/content/show.php/klicker?content=99554
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	99554-%{oname}%{version}.tar.gz
BuildRequires:	plasma-devel
Provides:	plasma-applet

%description
Klicker is an icon application launcher, with zoom


%prep
%setup -q -n %{oname}%{version}


%build
%cmake_kde4
%make

%install
rm -fr %buildroot
cd build
%{makeinstall_std}
cd -


%files
%defattr(-,root,root)

%{_libdir}/kde4/klicker.so
%{_kde_datadir}/kde4/services/plasma-applet-klicker.desktop


%clean
rm -rf "%{buildroot}"

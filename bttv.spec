
# conditional build
# _without_dist_kernel		without kernel from distribution

%define		_kernel_ver	%(grep UTS_RELEASE %{_kernelsrcdir}/include/linux/version.h 2>/dev/null | cut -d'"' -f2)
%define		_kernel_ver_str	%(echo %{_kernel_ver} | sed s/-/_/g)
%define		smpstr	%{?_with_smp:-smp}
%define		smp	%{?_with_smp:1}%{!?_with_smp:0}

Summary:	BrookTree TV tuner driver
Summary(pl):	Sterownik dla kart TV na chipsecie BrookTree
Name:		bttv
Version:	0.7.87
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	http://www.strusel007.de/linux/bttv/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://www.strusel007.de/linux/bttv/
%{!?_without_dist_kernel:BuildPrereq:	kernel-source}
ExclusiveArch:	%{ix86}
Requires:	i2c
PreReq:		modutils
BuildRequires:	i2c-devel
BuildConflicts:	kernel-source < 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel modules which add support for TV cards based on BrookTree BT
848 and 878 chips.

%description -l pl
Modu³y j±dra dodaj±ce obs³ugê kart TV na uk³adach BrookTree BT 848 i
878.

%package -n kernel%{smpstr}-misc-bttv
Summary:	Kernel modules for BrookTree TV tuner
Summary(pl):	Modu³y j±dra do obs³ugi tunerów TV BrookTree
Group:		Base/Kernel
Release:	%{release}@%{_kernel_ver_str}
PreReq:		modutils >= 2.4.6-4
%{!?_without_dist_kernel:Conflicts:	kernel < %{_kernel_ver}, kernel > %{_kernel_ver}}
%{!?_without_dist_kernel:Conflicts:	kernel-%{?_with_smp:up}%{!?_with_smp:smp}}
Requires:	%{name} = %{version}
Obsoletes:	bttv

%description -n kernel%{smpstr}-misc-bttv
Kernel modules which add support for TV cards based on BrookTree BT
848 and 878 chips.

%description -n kernel%{smpstr}-misc-bttv -l pl
Modu³y j±dra dodaj±ce obs³ugê kart TV na uk³adach BrookTree BT 848 i
878.

%package devel
Summary:	Header files for bttv
Summary(pl):	Pliki nag³ówkowe bttv
Group:		Development

%description devel
Header files for bttv.

%description devel -l pl
Pliki nag³ówkowe bttv.

%prep
%setup	-q
%patch0 -p1

%build
%{__make} EXTRA_CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C driver install DESTDIR=$RPM_BUILD_ROOT

%post
/sbin/depmod -a

%postun
/sbin/depmod -a

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kernel%{smpstr}-misc-bttv
%defattr(644,root,root,755)
/lib/modules/*/misc/*

%files
%defattr(644,root,root,755)
%doc CARDLIST Changes Insmod-options README* Sound-FAQ Specs Cards

%files devel
%defattr(644,root,root,755)
#/usr/src/linux/drivers/char/*

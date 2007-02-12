#
# TODO: UP/SMP (if this spec is useful for something now?)
#
# Conditional build:
%bcond_without	dist_kernel	# without kernel from distribution
#
%define		_kernel_ver	%(grep UTS_RELEASE %{_kernelsrcdir}/include/linux/version.h 2>/dev/null | cut -d'"' -f2)
%define		_kernel_ver_str	%(echo %{_kernel_ver} | sed s/-/_/g)
%define		smpstr	%{?with_smp:-smp}
%define		smp	%{?with_smp:1}%{!?with_smp:0}

Summary:	BrookTree TV tuner driver
Summary(pl.UTF-8):   Sterownik dla kart TV na chipsecie BrookTree
Name:		bttv
Version:	0.7.87
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	http://dl.bytesex.org/releases/video4linux/%{name}-%{version}.tar.gz
# Source0-md5:	61a0e73e433173c10b6edd2e9f27d69e
Patch0:		%{name}-Makefile.patch
URL:		http://linux.bytesex.org/v4l2/bttv.html
BuildRequires:	i2c-devel
%{?with_dist_kernel:BuildRequires: kernel-source}
BuildRequires:	rpmbuild(macros) >= 1.118
BuildConflicts:	kernel-source < 2.2.0
Requires:	i2c
Requires:	modutils
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel modules which add support for TV cards based on BrookTree BT
848 and 878 chips.

%description -l pl.UTF-8
Moduły jądra dodające obsługę kart TV na układach BrookTree BT 848 i
878.

%package -n kernel%{smpstr}-misc-bttv
Summary:	Kernel modules for BrookTree TV tuner
Summary(pl.UTF-8):   Moduły jądra do obsługi tunerów TV BrookTree
Release:	%{release}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires:	%{name} = %{version}-%{release}
Requires:	modutils >= 2.4.6-4
%{?with_dist_kernel:Conflicts:	kernel < %{_kernel_ver}, kernel > %{_kernel_ver}}
%{?with_dist_kernel:Conflicts:	kernel-%{?with_smp:up}%{!?with_smp:smp}}
Obsoletes:	bttv

%description -n kernel%{smpstr}-misc-bttv
Kernel modules which add support for TV cards based on BrookTree BT
848 and 878 chips.

%description -n kernel%{smpstr}-misc-bttv -l pl.UTF-8
Moduły jądra dodające obsługę kart TV na układach BrookTree BT 848 i
878.

%package devel
Summary:	Header files for bttv
Summary(pl.UTF-8):   Pliki nagłówkowe bttv
Group:		Development

%description devel
Header files for bttv.

%description devel -l pl.UTF-8
Pliki nagłówkowe bttv.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	EXTRA_CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C driver install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{smpstr}-misc-bttv
%depmod %{_kernel_ver}

%postun	-n kernel%{smpstr}-misc-bttv
%depmod %{_kernel_ver}

%files -n kernel%{smpstr}-misc-bttv
%defattr(644,root,root,755)
/lib/modules/*/misc/*

%files
%defattr(644,root,root,755)
%doc CARDLIST Changes Insmod-options README* Sound-FAQ Specs Cards

#%files devel
#%defattr(644,root,root,755)
#%{_kernelsrcdir}/drivers/char/*

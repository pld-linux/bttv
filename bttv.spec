Summary:	BrookTree TV tuner driver
Summary(pl):	Sterownik dla kart TV na chipsecie BrookTree
Name:		bttv
Version:	0.7.50
Release:	2
License:	GPL
Group:		Base/Kernel
Group(de):	Grundsätzlich/Kern
Group(pl):	Podstawowe/J±dro
Source0:	http://www.strusel007.de/linux/bttv/%{name}-%{version}.tar.gz
Patch0:		%{name}-Makefile.patch
URL:		http://www.strusel007.de/linux/bttv/
BuildPrereq:	kernel-headers
ExclusiveArch:	%{ix86}
Requires:	kernel(i2c)
Prereq:		modutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel modules which add support for TV cards based on BrookTree BT 848 and 878
chips.

%description -l pl
Modu³y j±dra dodaj±ce obs³ugê kart TV na uk³adach BrookTree BT 848 i 878.

%prep
%setup  -q
%patch0 -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CARDLIST Changes Insmod-options README* Sound-FAQ Specs

%post
/sbin/depmod -a

%postun
/sbin/depmod -a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/modules/misc/*
%doc *.gz

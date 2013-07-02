Name:       nemo-configs-n950-n9
Summary:    Some configs for n9/n950 adaptations
Version:    1
Release:    1
Group:      Configs
License:    GPLv2
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: oneshot
BuildRequires: repomd-pattern-builder
Requires:   oneshot
%{_oneshot_requires_post}

%description
%{summary}.

# Set the provides for package-groups/project-config once it's ready to replace old configuration packages
%package -n n950-n9-patterns
Summary:    Repository patterns for n950/n9 hw
#Provides:   package-groups

%description -n n950-n9-patterns
%{summary}.

%package -n n950-n9-prjconf
Summary:    Project configs for n950/n9 hw repos for OBS
#Provides:   project-config

%description -n n950-n9-prjconf
%{summary}.

%package wayland
Summary:    Repository patterns for n950/n9 hw
Provides:   ti-omap3-sgx-configs

%description wayland
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} ONESHOTDIR=%{_oneshotdir} install
/usr/bin/repomd-pattern-builder.py --patternxml -p ./patterns/ -o %{buildroot}/usr/share/package-groups/ --version=%{version} --release=%{release}

%files
%defattr(-,root,root,-)

%files -n n950-n9-patterns
%defattr(-,root,root,-)
%{_datadir}/package-groups/*.xml

%files -n n950-n9-prjconf
%defattr(-,root,root,-)
%{_datadir}/prjconf/*.xml

%files wayland
%{_sysconfdir}/powervr.ini
/var/lib/environment/compositor/60-n9-n950-ui.conf

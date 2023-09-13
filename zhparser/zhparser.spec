%global pname zhparser
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{pname}_%{pgmajorversion}
Version:	2.2
Release:	PIGSTY1%{?dist}
Summary:	Open-source full-text search of Chinese language
License:	PostgreSQL
URL:		https://github.com/amutu/zhparser/
Source0:	https://github.com/amutu/zhparser/archive/refs/tags/V2.2.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server scws

%description
zhparser is a PostgreSQL extension for full-text search of Chinese language (Mandarin Chinese).
It implements a Chinese language parser base on the Simple Chinese Word Segmentation(SCWS).

%prep
%setup -q -n %{pname}-%{version}

%build
PATH=%{pginstdir}/bin:$PATH %{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
PATH=%{pginstdir}/bin:$PATH %{__make} %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
%doc README.md
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%{pginstdir}/share/tsearch_data/dict.utf8.xdb
%{pginstdir}/share/tsearch_data/rules.utf8.ini
%exclude /usr/lib/.build-id/*
%exclude %{pginstdir}/lib/bitcode/zhparser*

%changelog
* Wed Sep 13 2023 Vonng <rh@vonng.com> - 2.2-1
- Initial RPM release
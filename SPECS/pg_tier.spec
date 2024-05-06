%define debug_package %{nil}
%global pname pg_tier
%global sname pg_tier
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.0.3
Release:	1PIGSTY%{?dist}
Summary:	Postgres Extension written in Rust, to enable data tiering to AWS S3
License:	Apache-2.0
URL:		https://github.com/tembo-io/pg_tier/%{sname}

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server
Recommends: parquet_s3_fdw_%{pgmajorversion}

%description
A Postgres extension to tier data to external storage

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_tier_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_tier.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_tier_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_tier-*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_tier_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_tier.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sun May 5 2024 Vonng <rh@vonng.com> - 0.0.3
- Initial RPM release, used by Pigsty <https://pigsty.io>
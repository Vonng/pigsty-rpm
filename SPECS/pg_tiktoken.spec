%define debug_package %{nil}
%global pname pg_tiktoken
%global sname pg_tiktoken
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.0.1
Release:	1PIGSTY%{?dist}
Summary:	OpenAI tiktoken tokenizer for postgres
License:	Apache-2.0
URL:		https://github.com/tembo-io/pg_tiktoken/%{sname}

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server

%description
Postgres extension that does input tokenization using OpenAI's tiktoken.

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/pg_tiktoken_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/pg_tiktoken.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/pg_tiktoken_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_tiktoken-*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/pg_tiktoken_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/pg_tiktoken.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sun May 5 2024 Vonng <rh@vonng.com> - 0.0.1
- Initial RPM release, used by Pigsty <https://pigsty.io>
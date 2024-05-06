%define debug_package %{nil}
%global pname vectorize
%global sname pg_vectorize
%global pginstdir /usr/pgsql-%{pgmajorversion}

Name:		%{sname}_%{pgmajorversion}
Version:	0.15.0
Release:	1PIGSTY%{?dist}
Summary:	A lightweight message queue. Like AWS SQS and RSMQ but on Postgres.
License:	Apache-2.0
URL:		https://github.com/tembo-io/pg_vectorize/%{sname}
#           https://github.com/tembo-io/pg_vectorize/archive/refs/tags/v0.15.0.tar.gz

BuildRequires:	postgresql%{pgmajorversion}-devel pgdg-srpm-macros >= 1.0.27
Requires:	postgresql%{pgmajorversion}-server pgmq_%{pgmajorversion} >= 1.1.1
Recommends: pg_cron_%{pgmajorversion}

%description
Postgres Message Queue (pg_vectorize) -- A lightweight message queue. Like AWS SQS and RSMQ but on Postgres.
Lightweight - No background worker or external dependencies, just Postgres functions packaged in an extension
Guaranteed "exactly once" delivery of messages to a consumer within a visibility timeout
API parity with AWS SQS and RSMQ
Messages stay in the queue until explicitly removed
Messages can be archived, instead of deleted, for long-term retention and replayability

%install
%{__rm} -rf %{buildroot}
install -d %{buildroot}%{pginstdir}/lib/
install -d %{buildroot}%{pginstdir}/share/extension/
install -m 755 %{_sourcedir}/vectorize_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/lib/vectorize.so %{buildroot}%{pginstdir}/lib/
install -m 644 %{_sourcedir}/vectorize_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/vectorize-*.sql %{buildroot}%{pginstdir}/share/extension/
install -m 644 %{_sourcedir}/vectorize_%{pgmajorversion}/usr/pgsql-%{pgmajorversion}/share/extension/vectorize.control %{buildroot}%{pginstdir}/share/extension/

%files
%{pginstdir}/lib/%{pname}.so
%{pginstdir}/share/extension/%{pname}.control
%{pginstdir}/share/extension/%{pname}*sql
%exclude /usr/lib/.build-id

%changelog
* Sun May 5 2024 Vonng <rh@vonng.com> - 0.15.0
- Initial RPM release, used by Pigsty <https://pigsty.io>
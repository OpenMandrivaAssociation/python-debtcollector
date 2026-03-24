%define module debtcollector

Name:		python-debtcollector
Version:	3.1.0
Release:	1
Summary:	A collection of Python deprecation patterns and strategies
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/debtcollector/
Source0:	https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
A collection of Python deprecation patterns and strategies that help you
collect your technical debt in a non-destructive manner.

The goal of this library is to provide well documented developer facing
deprecation patterns that start of with a basic set and can expand into a
larger set of patterns as time goes on.

The desired output of these patterns is to apply the warnings module to
emit DeprecationWarning, PendingDeprecationWarning or similar derivative
to developers using libraries (or potentially applications) about future
deprecations.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info

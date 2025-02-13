Name:		python-debtcollector
Version:	3.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/debtcollector/debtcollector-%{version}.tar.gz
Summary:	A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.
URL:		https://pypi.org/project/debtcollector/
License:	GPL
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
A collection of Python deprecation patterns and strategies that help you collect your technical debt in a non-destructive manner.

%files
%{py_sitedir}/debtcollector
%{py_sitedir}/debtcollector-*.*-info

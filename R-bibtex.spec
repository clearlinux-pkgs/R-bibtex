#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-bibtex
Version  : 0.4.2
Release  : 8
URL      : https://cran.r-project.org/src/contrib/bibtex_0.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/bibtex_0.4.2.tar.gz
Summary  : Bibtex Parser
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bibtex-lib
Requires: R-stringi
BuildRequires : R-stringi
BuildRequires : clr-R-helpers

%description
# bibtex
[![Travis-CI Build Status](https://travis-ci.org/romainfrancois/bibtex.svg?branch=master)](https://travis-ci.org/romainfrancois/bibtex)

%package lib
Summary: lib components for the R-bibtex package.
Group: Libraries

%description lib
lib components for the R-bibtex package.


%prep
%setup -q -c -n bibtex

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523290867

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523290867
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bibtex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bibtex
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library bibtex
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library bibtex|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/bibtex/DESCRIPTION
/usr/lib64/R/library/bibtex/INDEX
/usr/lib64/R/library/bibtex/Meta/Rd.rds
/usr/lib64/R/library/bibtex/Meta/features.rds
/usr/lib64/R/library/bibtex/Meta/hsearch.rds
/usr/lib64/R/library/bibtex/Meta/links.rds
/usr/lib64/R/library/bibtex/Meta/nsInfo.rds
/usr/lib64/R/library/bibtex/Meta/package.rds
/usr/lib64/R/library/bibtex/NAMESPACE
/usr/lib64/R/library/bibtex/NEWS.Rd
/usr/lib64/R/library/bibtex/R/bibtex
/usr/lib64/R/library/bibtex/R/bibtex.rdb
/usr/lib64/R/library/bibtex/R/bibtex.rdx
/usr/lib64/R/library/bibtex/REFERENCES.bib
/usr/lib64/R/library/bibtex/bib/badFormat.bib
/usr/lib64/R/library/bibtex/bib/base.bib
/usr/lib64/R/library/bibtex/bib/datasets.bib
/usr/lib64/R/library/bibtex/bib/grDevices.bib
/usr/lib64/R/library/bibtex/bib/graphics.bib
/usr/lib64/R/library/bibtex/bib/methods.bib
/usr/lib64/R/library/bibtex/bib/stats.bib
/usr/lib64/R/library/bibtex/bib/stats4.bib
/usr/lib64/R/library/bibtex/bib/tools.bib
/usr/lib64/R/library/bibtex/bib/utils.bib
/usr/lib64/R/library/bibtex/bibparse.output
/usr/lib64/R/library/bibtex/clean-bibtex.R
/usr/lib64/R/library/bibtex/grammar.output
/usr/lib64/R/library/bibtex/grammar/biblex.l
/usr/lib64/R/library/bibtex/grammar/bibparse.y
/usr/lib64/R/library/bibtex/help/AnIndex
/usr/lib64/R/library/bibtex/help/aliases.rds
/usr/lib64/R/library/bibtex/help/bibtex.rdb
/usr/lib64/R/library/bibtex/help/bibtex.rdx
/usr/lib64/R/library/bibtex/help/paths.rds
/usr/lib64/R/library/bibtex/html/00Index.html
/usr/lib64/R/library/bibtex/html/R.css
/usr/lib64/R/library/bibtex/include/bibparse.h
/usr/lib64/R/library/bibtex/include/bibtex.h
/usr/lib64/R/library/bibtex/libs/symbols.rds
/usr/lib64/R/library/bibtex/objects.output

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/bibtex/libs/bibtex.so
/usr/lib64/R/library/bibtex/libs/bibtex.so.avx2
/usr/lib64/R/library/bibtex/libs/bibtex.so.avx512

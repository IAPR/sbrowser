# Maintainer: Ivan Pacheco (Kinokoio) <kinokoio@hotmail.com>

pkgname=sbrowser
pkgver=0.0.1
pkgrel=1
pkgdesc="Simple browser based on PyQt5 and QtWebKit"
arch=(any)
url="https://github.com/kinokoio/sbrowser"
license=('GPL')
depends=('python>=3.4' 'python-pyqt5>=5.2' 'qt5-base>=5.2'
         'qt5-webkit>=5.2')
makedepends('coreutils' 'git')
source=("git+https://github.com/kinokoio/sbrowser.git")
sha256sums=("SKIP")

build() {
    cd "$srcdir"
    python setup.py build
}

package() {
    cd "$srcdir"
    python setup.py install 
    mkdir /usr/share/doc/sbrowser
    cp LICENSE README.md /usr/share/doc/sbrowser
}

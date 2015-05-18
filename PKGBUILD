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
makedepends=('coreutils' 'git')
source=("git+https://github.com/kinokoio/sbrowser")
sha256sums=("SKIP")

package() {
    cd "$srcdir/$pkgname"
    python setup.py install --root="$pkgdir/" --optimize=1
    install -Dm755 LICENSE $pkgdir/usr/share/doc/$pkgname/LICENSE
    install -Dm755 README.md $pkgdir/usr/share/doc/$pkgname/README
}

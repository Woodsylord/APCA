
#!/bin/bash
find /home/arma3server/arma3server/serverfiles/cmods -depth -exec rename 's/(.*)/\L$1/' {} \;
find /home/arma3server/arma3server/serverfiles/omods -depth -exec rename 's/(.*)/\L$1/' {} \;
find /home/arma3server/arma3server/serverfiles/cmods -depth -name "* *" -exec rename 's/ /_/g' {} \;
find /home/arma3server/arma3server/serverfiles/omods -depth -name "* *" -exec rename 's/ /_/g' {} \;

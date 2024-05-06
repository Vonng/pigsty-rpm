# Parquet S3 FDW


```bash
sudo dnf install \
     cmake \
     gcc \
     gcc-c++ \
     ninja-build \
     make
     
cd arrow/cpp
cmake --list-presets
cmake --preset -N ninja-release

cmake --preset ninja-release


cd ~/
git clone git@github.com:apache/arrow.git
mkdir -p arrow/cpp/release
cd ~/arrow/cpp/release

cmake .. -DARROW_PARQUET=ON -DARROW_S3=ON
make -j8
```





## AWS CPP SDK

https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/setup-linux.html

```bash
sudo yum install libcurl-devel openssl-devel libuuid-devel pulseaudio-libs-devel

git clone --recurse-submodules https://github.com/aws/aws-sdk-cpp
git clone --recurse-submodules git@github.com:aws/aws-sdk-cpp.git

cd aws-sdk-cpp; mkdir release; cd release;
cmake .. -DBUILD_ONLY="s3"
make -j8
```



## prepare

```bash
cd ~/; mkdir libarrow-s3; cd libarrow-s3;
cp ~/aws-sdk-cpp/sdk_build/src/aws-cpp-sdk-core/libaws-cpp-sdk-core.so       ~/libarrow-s3/libaws-cpp-sdk-core.so;
cp ~/aws-sdk-cpp/sdk_build/generated/src/aws-cpp-sdk-s3/libaws-cpp-sdk-s3.so ~/libarrow-s3/libaws-cpp-sdk-s3.so;
cp -d ~/arrow/cpp/release/release/*                                          ~/libarrow-s3/;
rm -rf *.a

sudo yum install patchelf



patchelf --remove-rpath libarrow.so.1700.0.0
patchelf --remove-rpath libparquet.so.1700.0.0
patchelf --remove-rpath libaws-cpp-sdk-core.so
patchelf --remove-rpath libaws-cpp-sdk-s3.so

rm -rf ~/rpmbuild/SOURCES/libarrow-s3; cp -r ~/libarrow-s3 ~/rpmbuild/SOURCES/libarrow-s3

cd ~/rpmbuild/SPECS
```


```bash
rpmbuild -ba ~/rpmbuild/SPECS/libarrow-s3.spec
sudo rpm -ivh ~/rpmbuild/RPMS/x86_64/libarrow-s3-17.0.0-1PIGSTY.*

rpmbuild --define "pgmajorversion 16" -ba ~/rpmbuild/SPECS/parquet_s3_fdw.spec

#rpmbuild --define "pgmajorversion 15" -ba ~/rpmbuild/SPECS/parquet_s3_fdw.spec
#rpmbuild --define "pgmajorversion 13" -ba ~/rpmbuild/SPECS/parquet_s3_fdw.spec
#rpmbuild --define "pgmajorversion 14" -ba ~/rpmbuild/SPECS/parquet_s3_fdw.spec
```
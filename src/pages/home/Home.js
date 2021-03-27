import Search from '../../components/search/index.js';
import RecipeReviewCard from '../../components/card/index.js';
import React, { useState } from "react";
import "./style.css"

const kliniks = [
    {
        id: "1",
        name: "hoffmann",
        address: "hospital address1",
        rating: 3,
        ratingNumber: "24",
        image: "https://www.deutsches-krankenhaus-verzeichnis.de/app/file/image/show/039d2d2d7948ef77_d08ce7f2-cdce-449d-a8fb-f11ed90eb888.png"
    },
    {
        id: "2",
        name: "marienstift",
        address: "hospital address2",
        rating: 4,
        ratingNumber: "78",
        image: "https://www.neuerkerode.de/fileadmin/_processed_/c/f/csm_DC42536_b9d7705da0.jpg"
    },
    {
        id: "3",
        name: "herzogin",
        address: "hospital address3",
        rating: 4.3,
        ratingNumber: "111",
        image: "https://cdn.regionalheute.de/images/2020/1/164/1000/911d87ffacaa43af8af14585e8584631.jpg"
    },
    {
        id: "4",
        name: "asklepios göttingen",
        address: "hospital address4",
        rating: 3.5,
        ratingNumber: "141",
        image: "https://upload.wikimedia.org/wikipedia/commons/4/49/Asklepios_Fachklinikum_G%C3%B6ttingen_%281%29.JPG"
    },
    {
        id: "5",
        name: "asklepios tiefenbrunn",
        address: "hospital address5",
        rating: 5,
        ratingNumber: "119",
        image: "https://www.deutsches-krankenhaus-verzeichnis.de/app/file/image/show/ea64d9b452af986d_03e784fd-db0c-4ddf-b854-ff6cf6fbf326.png"
    },
    {
        id: "6",
        name: "friederikenstift",
        address: "hospital address6",
        rating: 1,
        ratingNumber: "211",
        image: "https://upload.wikimedia.org/wikipedia/commons/c/c6/Friederikenstift_Hannover.jpg"
    },
    {
        id: "7",
        name: "annastift",
        address: "hospital address7",
        rating: 1.3,
        ratingNumber: "991",
        image: "https://img.fotocommunity.com/annastift-i-hannover-9d4296bf-246d-4e54-ba00-12cc31f8294e.jpg?width=1000"
    },
    {
        id: "8",
        name: "clementinhaus",
        address: "hospital address8",
        rating: 4.9,
        ratingNumber: "181",
        image: "https://www.clementinenhaus.de/images/1920x500_wo/Clementinenhaus_wo.jpg"
    },
    {
        id: "9",
        name: "sophienklinik",
        address: "hospital address9",
        rating: 4.9,
        ratingNumber: "181",
        image: "https://www.sophienklinik.de/wp-content/uploads/2018/05/sk_header_kontakt_neu.jpg"
    },
    {
        id: "10",
        name: "KRH großburgwedel",
        address: "hospital address10",
        rating: 4.9,
        ratingNumber: "181",
        image: "https://www.hannover.de/var/storage/images/_aliases/alias_300x225px/media/01-data-neu/bilder/bilder-region-hannover/geb%C3%A4ude-der-region/klinikum-der-region-hannover/krh_klinikum_grossburgwedel/10578457-1-ger-DE/KRH_Klinikum_Grossburgwedel.jpg"
    },
    {
        id: "11",
        name: "KRH lehrte",
        address: "hospital address11",
        rating: 4.9,
        ratingNumber: "181",
        image: "https://lehrte.krh.de/fileadmin/_processed_/5/2/csm_lehrte_787x300_763a970c44.jpg"
    }
]

const Home = (props) => {
    const copyKliniklist = [...kliniks];
    const [kliniklist, setKlinikList] = useState([...kliniks]);

    const filterKliniks = (e) => {
        console.log("searched: " + e);
        const filteredKliniks = copyKliniklist.filter((item) => {
            const searchedKlinikUpper = e?.toUpperCase();
            const kliniksName = item.name.toUpperCase();
            return kliniksName.indexOf(searchedKlinikUpper) > -1;
        });
        setKlinikList(filteredKliniks);
    };
    return (
        <div id="homepage">
            <div id="searcharea">
                <p>Find best clinic around</p>
                <Search searchedText={filterKliniks} />
            </div>


            <div id="cards">
                {kliniklist?.map((k) => (
                    //console.log(`rating of hospital${k.id}: ${k.rating}`);
                    //<><div>{k.address}</div>
                    //<div>{k.rating}</div></>
                    <RecipeReviewCard id={k.id} name={k.name} address={k.address} rating={k.rating} ratingNumber={k.ratingNumber} image={k.image} />
                ))}
            </div>

        </div>
    )
}

export default Home



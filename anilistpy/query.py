
EPISODE_NUMS = '''
query($id: Int) {
    Media(id: $id, type: ANIME) {
        streamingEpisodes {
            title
            url
            thumbnail
            site
        }
    }
}
'''

USERDATA = '''
query ($username: String, $type: MediaType) {
    MediaListCollection(userName: $username, type: $type) {
        user {
            id
            name
            siteUrl
            avatar {
                large
            }
        }
        lists {
            name
            status
            entries {
                id
                status
                progress
                media {
                    id
                    idMal
                    title {
                        english
                        romaji
                        userPreferred
                    }
                    status
                    genres
                }
                score(format: POINT_10)
                notes
                repeat
            }
        }
    }
}
'''

ANIME_ID = '''
query($id: Int) {
    Media(id: $id, type: ANIME) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
        }
        coverImage {
            extraLarge
        }
        bannerImage
        description
        favourites
        popularity
        genres
        type
        format
        episodes
        season
        seasonYear
        status
        averageScore
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        trailer {
            id
        }
        studios {
            nodes {
                name
            }
        }
        tags {
            name
        }
        characters {
            nodes {
                image {
                    large
                }
                siteUrl
            }
        }
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

ANIME_IDMAL = '''
query($idMal: Int) {
    Media(idMal: $idMal, type: ANIME) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
        }
        coverImage {
            extraLarge
        }
        bannerImage
        description
        favourites
        popularity
        genres
        type
        format
        episodes
        season
        seasonYear
        status
        averageScore
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        trailer {
            id
        }
        studios {
            nodes {
                name
            }
        }
        tags {
            name
        }
        characters {
            nodes {
                image {
                    large
                }
                siteUrl
            }
        }
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

ANIME_SEARCH = '''
query($search: String) {
    Media(search: $search, type: ANIME) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
        }
        coverImage {
            extraLarge
        }
        bannerImage
        description
        favourites
        popularity
        genres
        type
        format
        episodes
        season
        seasonYear
        status
        averageScore
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        studios {
            nodes {
                name
            }
        }
        tags {
            name
        }
        characters {
            nodes {
                image {
                    large
                }
                siteUrl
            }
        }
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MANGA_ID = '''
query($id: Int) {
    Media (id: $id, type: MANGA) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
            native
            userPreferred
        }
        coverImage {
            extraLarge
        }
        startDate {
            year
            month
            day
        }
        bannerImage
        isAdult
        description
        favourites
        popularity
        genres
        type
        format
        chapters
        volumes
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        status
        averageScore
        tags {
            id
            name
            isAdult
            isMediaSpoiler
            isGeneralSpoiler
        }
        trailer {
            id
            thumbnail
            site
        }
        characters {
            nodes {
                name {
                    first
                    middle
                    last
                    full
                    native
                    userPreferred
                }
                gender
                age
                dateOfBirth {
                    year
                    month
                    day
                }
                image {
                    large
                }
                siteUrl
            }
        }
        staff {
            edges {
                id
                node {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    gender
                    description
                    bloodType
                    yearsActive
                    modNotes
                    homeTown
                }
            }
        }
        isLicensed
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MANGA_IDMAL = '''
query($idMal: Int) {
    Media (idMal: $idMal, type: MANGA) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
            native
            userPreferred
        }
        coverImage {
            extraLarge
        }
        startDate {
            year
            month
            day
        }
        bannerImage
        isAdult
        description
        favourites
        popularity
        genres
        type
        format
        chapters
        volumes
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        status
        averageScore
        tags {
            id
            name
            isAdult
            isMediaSpoiler
            isGeneralSpoiler
        }
        trailer {
            id
            thumbnail
            site
        }
        characters {
            nodes {
                name {
                    first
                    middle
                    last
                    full
                    native
                    userPreferred
                }
                gender
                age
                dateOfBirth {
                    year
                    month
                    day
                }
                image {
                    large
                }
                siteUrl
            }
        }
        staff {
            edges {
                id
                node {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    gender
                    description
                    bloodType
                    yearsActive
                    modNotes
                    homeTown
                }
            }
        }
        isLicensed
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''

MANGA_SEARCH = '''
query($search: String) {
    Media (search: $search, type: MANGA) {
        siteUrl
        id
        idMal
        title {
            english
            romaji
            native
            userPreferred
        }
        coverImage {
            extraLarge
        }
        startDate {
            year
            month
            day
        }
        bannerImage
        isAdult
        description
        favourites
        popularity
        genres
        type
        format
        chapters
        volumes
        airingSchedule {
            edges {
                id
                node {
                    media {
                        id
                    }
                    episode
                    airingAt
                }
            }
        }
        status
        averageScore
        tags {
            id
            name
            isAdult
            isMediaSpoiler
            isGeneralSpoiler
        }
        trailer {
            id
            thumbnail
            site
        }
        characters {
            nodes {
                name {
                    first
                    middle
                    last
                    full
                    native
                    userPreferred
                }
                gender
                age
                dateOfBirth {
                    year
                    month
                    day
                }
                image {
                    large
                }
                siteUrl
            }
        }
        staff {
            edges {
                id
                node {
                    name {
                        first
                        middle
                        last
                        full
                        native
                        userPreferred
                    }
                    dateOfBirth {
                        year
                        month
                        day
                    }
                    gender
                    description
                    bloodType
                    yearsActive
                    modNotes
                    homeTown
                }
            }
        }
        isLicensed
        relations {
            nodes {
                coverImage {
                    extraLarge
                }
                siteUrl
            }
        }
        trailer {
            id
            site
            thumbnail
        }
        recommendations {
            nodes {
                mediaRecommendation {
                    siteUrl
                    coverImage {
                        extraLarge
                    }
                }
            }
        }
    }
}
'''